rest: demonstrates RESTful web services with CXF
===============================================
Author: Fuse Team  
Level: Beginner  
Technologies: Fuse, OSGi, CXF  
Summary: Demonstrates RESTful web services with CXF  
Target Product: Fuse  
Source: <https://github.com/jboss-fuse/quickstarts>

What is it?
-----------
This quick start demonstrates how to create a RESTful (JAX-RS) web service using CXF and expose it with the OSGi HTTP Service.

In studying this quick start you will learn:

* how to configure the JAX-RS web services by using the blueprint configuration file.
* how to use JAX-RS annotations to map methods and classes to URIs
* how to use JAXB annotations to define beans and output XML responses
* how to use the JAX-RS API to create HTTP responses

For more information see:

* <https://access.redhat.com/site/documentation/JBoss_Fuse/> for more information about using JBoss Fuse

Build and Deploy the Quickstart
-------------------------------

* Modify a file in the project (for example this readme).
* Commit in the change using `git commit -am "triggering build"`
* Push the change using `git push`
* The builder cart should build and deploy the project.
* Assign the my-rest-quickstart profile to a FUSE container.

Use the bundle
--------------

### Browsing Web service metadata

A full listing of all CXF web services is available at

    http://${fuse-app}/cxf

After you deployed this quick start, you will see the following endpoint address appear in the 'Available RESTful services' section:

    http://${fuse-app}/cxf/crm
**Note:**: Don't try to access this endpoint address from browser, as it's inaccessible by design

Just below it, you'll find a link to the WADL describing all the root resources:

    http://${fuse-app}/cxf/crm?_wadl

You can also look at the more specific WADL, the only that only lists information about 'customerservice' itself:

	http://l${fuse-app}/cxf/crm/customerservice?_wadl&_type=xml

### Access services using a web browser

You can use any browser to perform a HTTP GET.  This allows you to very easily test a few of the RESTful services we defined:

Use this URL to display the XML representation for customer 123:

    http://${fuse-app}/cxf/crm/customerservice/customers/123

You can also access the XML representation for order 223 ...

    http://${fuse-app}/cxf/crm/customerservice/orders/223

... or the XML representation of product 323 in order 223 with

    http://${fuse-app}/cxf/crm/customerservice/orders/223/products/323

**Note:** if you use Safari, you will only see the text elements but not the XML tags - you can view the entire document with 'View Source'

### To run the tests:

In this quick start project, we also provide integration tests which perform a few HTTP requests to test our Web services. We
created a Maven `test` profile to allow us to run tests code with a simple Maven command after having deployed the bundle to Fuse:

1. Change to the `rest` directory.
2. Run the following command:

        mvn -Ptest
        
The tests in `src/test/java/org.jboss.quickstarts.fuse.rest/CrmTest`  make a sequence of RESTful invocations and displays the results.

### To run a command-line utility:

You can use a command-line utility, such as cURL or wget, to perform the HTTP requests.  We have provided a few files with sample XML representations in `src/test/resources`, so we will use those for testing our services.

1. Open a command prompt and change directory to `rest`.
2. Run the following curl commands (curl commands may not be available on all platforms):
    
    * Create a customer
 
            curl -X POST -T src/test/resources/add_customer.xml -H "Content-Type: text/xml" http://${fuse-app}/cxf/crm/customerservice/customers
  
    * Retrieve the customer instance with id 123
    
            curl http://${fuse-app}/cxf/crm/customerservice/customers/123

    * Update the customer instance with id 123
  
            curl -X PUT -T src/test/resources/update_customer.xml -H "Content-Type: text/xml" http://${fuse-app}/cxf/crm/customerservice/customers

    * Delete the customer instance with id 123
  
             curl -X DELETE http://${fuse-app}/cxf/crm/customerservice/customers/123


Undeploy the Bundle
-------------------

To stop and undeploy the project in Fuse:

1. Remove the my-rest-quickstart profile from the FUSE container.



