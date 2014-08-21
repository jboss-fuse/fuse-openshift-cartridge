Running Red Hat JBoss AMQ on OpenShift
-------------------------

If you want to try out Red Hat JBoss AMQ on OpenShift here's the current instructions:

### 1. Create the Red Hat JBoss AMQ cartridge (based on EA 6.1 build of JBoss Red Hat JBoss AMQ).

If you want to use the [OpenShift create application page](https://openshift.redhat.com/app/console/application_types), enter the cartridge URI of **http://is.gd/Q5ihum** in the entry field (at the bottom left of the form).

Or if you want to use the [rhc command line](https://www.openshift.com/developers/rhc-client-tools-install) type:

    rhc create-app amq http://is.gd/Q5ihum

This will output the generated user-id/password, http management url and public self-signed certificate for the AMQ server.  Make sure you copy and save all that information.  You will need it later to connect messaging clients to the server.

If you prefer to specify your own password (which can be handy in development to reuse the same password across fabrics) try this:

    rhc create-app -e OPENSHIFT_FUSE_PASSWORD=password amq http://is.gd/Q5ihum

You probably want to use a safer password than 'password' though ;)

If you have a subscription for Openshift that gives you access to other gear sizes, you could run 

    rhc create-app -g medium -e OPENSHIFT_FUSE_PASSWORD=password amq http://is.gd/Q5ihum

That will create the container in an Openshift gear of the specified size.

You can then login to your registry at: **http://amq-$USERID.rhcloud.com/hawtio/** where $USERID is your openshift account name. Use the following login:

```
user:     admin
password: $password
```

### 2. Open the **Red Hat JBoss AMQ** Console and you should be able to see the ActiveMQ tab.

You can now use the Runtime and Configuration tabs and create containers etc.

### 3. Connecting Messaging Clients

Messaging clients MUST use SSL/TLS and set the SNI SSL header.  All client libraries proved by AMQ 6.1 set this header when connecting via SSL.  The JVM only supports setting the SNI header as of Java 7.

By default the the following protocols and ports are available for clients to connect to:

* Openwire: `2303`
* STOMP: `2304`
* AMQP 1.0: `2305`
* MQTT 3.1: `2306`

#### Updating a AMQ 6.1 JMS client to connect to AMQ 6.1 on OpenShift

1. Update the code that creates the JMS connection:

        ActiveMQConnectionFactory factory = new ActiveMQConnectionFactory("ssl://amq-$USERID.rhcloud.com:2303");
        Connection connection = factory.createConnection("admin", "$password");

2. Store the server's public self-signed certificate in a file called `server.crt`.  Then create a Java key store that imports the cert:   

        $ keytool -importcert -keystore my.jks -storepass password \
            -file server.crt -noprompt

3. Configure the JVM to use the key store:   

        $ java -Djavax.net.ssl.trustStore=my.jks ...          




