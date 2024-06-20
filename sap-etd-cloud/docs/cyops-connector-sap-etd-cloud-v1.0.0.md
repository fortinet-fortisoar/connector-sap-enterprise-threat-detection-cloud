## About the connector
SAP Enterprise Threat Detection (ETD), Cloud Edition helps you to identify the real attacks as they are happening and analyze the threats quickly enough to neutralize them before serious damage occurs. SAP Enterprise Threat Detection Cloud Edition connector performs action like get and ingest Events, Alerts and Investigations.
<p>This document provides information about the SAP Enterprise Threat Detection Cloud Edition Connector, which facilitates automated interactions, with a SAP Enterprise Threat Detection Cloud Edition server using FortiSOAR&trade; playbooks. Add the SAP Enterprise Threat Detection Cloud Edition Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with SAP Enterprise Threat Detection Cloud Edition.</p>

### Version information

Connector Version: 1.0.0


Authored By: Fortinet CSE

Certified: No
## Installing the connector
<p>From FortiSOAR&trade; 5.0.0 onwards, use the <strong>Connector Store</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.<br>You can also use the following <code>yum</code> command as a root user to install connectors from an SSH session:</p>
`yum install cyops-connector-sap-etd-cloud`

## Prerequisites to configuring the connector
- You must have the URL of SAP Enterprise Threat Detection Cloud Edition server to which you will connect and perform automated operations and credentials to access that server.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the SAP Enterprise Threat Detection Cloud Edition server.

## Minimum Permissions Required
- N/A

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>SAP Enterprise Threat Detection Cloud Edition</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations&nbsp;</strong> tab enter the required configuration details:&nbsp;</p>
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Authentication URL<br></td><td><br>
<tr><td>ETD Data Retrieval URL<br></td><td><br>
<tr><td>Client ID<br></td><td><br>
<tr><td>Client Secret<br></td><td><br>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function<br></th><th>Description<br></th><th>Annotation and Category<br></th></tr></thead><tbody><tr><td>Get Alerts<br></td><td>Retrive alerts based on start and end date/time.<br></td><td> <br/><br></td></tr>
<tr><td>Get Alert Details by ID<br></td><td>Get Alerts by specified ID<br></td><td> <br/><br></td></tr>
<tr><td>Get Investigations<br></td><td>Get alerts with expansion and filter for investigations<br></td><td> <br/><br></td></tr>
</tbody></table>

### operation: Get Alerts
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Limit<br></td><td>Specify the amount of results which will be returned.<br>
</td></tr><tr><td>Start Time<br></td><td>Specify the Date and Time from which the alerts should be recieved from.<br>
</td></tr><tr><td>End Time<br></td><td>Specify the Date and Time from which the alerts should be recieved to.<br>
</td></tr></tbody></table>

#### Output

 No output schema is available at this time.

### operation: Get Alert Details by ID
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Alert ID<br></td><td>Specify Alert ID to retrieve details.<br>
</td></tr></tbody></table>

#### Output

 No output schema is available at this time.

### operation: Get Investigations
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Alert ID<br></td><td>Alert ID to filter Investigations for<br>
</td></tr><tr><td>Limit<br></td><td>Limit the amount of results<br>
</td></tr></tbody></table>

#### Output

 No output schema is available at this time.

## Included playbooks
The `Sample - sap-etd-cloud - 1.0.0` playbook collection comes bundled with the SAP Enterprise Threat Detection Cloud Edition connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR<sup>TM</sup> after importing the SAP Enterprise Threat Detection Cloud Edition connector.

- > SAP ETD CE > Create Record
- > SAP ETD CE > Fetch
- Get Alert Details by ID
- Get Alerts
- Get Investigations
- SAP ETD CE > Ingest

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection, since the sample playbook collection gets deleted during connector upgrade and delete.
## Data Ingestion Support
Use the Data Ingestion Wizard to easily ingest data into FortiSOAR&trade; by pulling events/alerts/incidents, based on the requirement.

**TODO:** provide the list of steps to configure the ingestion with the screen shots and limitations if any in this section.