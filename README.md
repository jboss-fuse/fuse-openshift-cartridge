Running Fuse on OpenShift
-------------------------

If you want to try out Fuse on OpenShift here's the current instructions:

### 1 Create the Fuse cartridge (based on EA 6.1 build of JBoss Fuse).

If you use the web UI to create an application then enter the cartridge URI of **https://raw.github.com/jboss-fuse/fuse-openshift-cartridge/master/metadata/manifest.yml** in the entry field (at the bottom left of the form).

Or if you want to use the [rhc command line](https://www.openshift.com/developers/rhc-client-tools-install) type:

    rhc create-app fuse https://raw.github.com/jboss-fuse/fuse-openshift-cartridge/master/metadata/manifest.yml

This will output the generated password for fabric and also the http
url for hawtio.

If you prefer to specify your own password (which can be handy in development to reuse the same password across fabrics) try this:

    rhc create-app -e OPENSHIFT_FUSE_ZOOKEEPER_PASSWORD=admin fuse https://raw.github.com/jboss-fuse/fuse-openshift-cartridge/master/metadata/manifest.yml

You probably want to use a safer password than 'admin' though ;)

If you have a subscription for Openshift that gives you access to other gear sizes, you could run 

    rhc create-app -g medium -e OPENSHIFT_FUSE_ZOOKEEPER_PASSWORD=admin fuse https://raw.github.com/jboss-fuse/fuse-openshift-cartridge/master/metadata/manifest.yml
    
That will create the container in an Openshift gear of the specified size.

You can then login to your registry at: **http://fuse-$USERID.rhcloud.com/hawtio/** where $USERID is your openshift account name. Use the following login:

```
user:     admin
password: $password
```

### 2 Open the **Fabric** tab and you should be able to see the containers running (only 1 at the moment).

### 3 click on the + icon on the Containers tab to add a new container using the openshift creation form

Enter something like these details:

```
name:      someContainerName
serverUrl: openshift.redhat.com
login:     myname@foo.com
password:  *********
domain:    mydomain
```

### Using different versions of Fuse

Until we get to 6.1 GA we are doing continuous deployment builds of Fuse 6.1 used by the cartridge.

The [URL for the cartridge](https://raw.github.com/jboss-fuse/fuse-openshift-cartridge/master/metadata/manifest.yml) is really just from the master branch of this github project.

Though we create a branch for every distro of Fuse 6.1 beta; so you can always specify the exact build you want to use.

e.g. click on the branches button on github, or here's the [build 169 branch in github](https://github.com/jboss-fuse/fuse-openshift-cartridge/blob/jboss-fuse-6.1.x-169/metadata/manifest.yml) then to get the URL for this just click the [RAW link](https://raw.github.com/jboss-fuse/fuse-openshift-cartridge/jboss-fuse-6.1.x-170/metadata/manifest.yml) to get the URL you can use with OpenShift; either via the website or the **rhc** command line tool.
