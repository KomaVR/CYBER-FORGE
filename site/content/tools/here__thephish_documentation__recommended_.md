---
title: "here (ThePhish documentation, recommended)"
description: "
Configuration
The file configuration.json is the global configuration file that allows setting the parameters for the connection to the mailbox and to the instances of TheHive, Cortex and MISP. It also allows setting parameters related to the cases that will be created on TheHive.
{
	\"imap\" : {
		\"host\" : \"imap.gmail.com\",
		\"port\" : \"993\",
		\"user\" : \"\",
		\"password\" : \"\",
		\"folder\" : \"inbox\"
	},
	\"thehive\" : {
		\"url\" : \"http://thehive:9000\",
		\"apikey\" : \"\"
	},
	\"cortex\" : {
		\"url\" : \"http://cortex:9001\",
		\"apikey\" : \"\",
		\"id\" : \"local\"
	},
	\"misp\" : {
		\"id\" : \"MISP THP\"
	},
	\"case\" : {
		\"tlp\" : \"2\",
		\"pap\" : \"2\",
		\"tags\" : [\"email\", \"ThePhish\"]
	}
}

In the imap part, if you are using a Gmail address, you only need to set the username used to connect to the IMAP server (which is your email address) and the app password.
In the thehive part you have to set the URL at which the TheHive instance is reachable and set the API key of the user created on TheHive that ThePhish will use to interact with TheHive.
In the cortex part you have to set the URL at which the Cortex instance is reachable and set the API key of the user created on Cortex that both ThePhish and TheHive will use to interact with Cortex. Moreover, you have to set the ID given to the Cortex instance.
In the misp part you only have to set the ID given to the MISP instance.
In the case part you can set the default TLP and PAP levels for the cases created by ThePhish and also the tags that will be applied to them at their creation.

You can learn how to create an organization and a user with org-admin role in that organization on TheHive and obtain its API key  or here (TheHive documentation). Similarly, you can learn how to create an organization and a user with read, analyze roles in that organization on Cortex and obtain its API key  or here (Cortex documentation).
The URLs and the IDs that are set in this file must be the same that are set in the configuration file of TheHive named application.conf, which contains a part related to Cortex and a part related to MISP. The parameters that you should look for are name and url in both parts, which correspond to the IDs and the URLs of the Cortex and MISP instances. The IDs can also be found in the About window on the web interface of TheHive. An example where the Cortex ID is the string local and the MISP ID is the string MISP THP is shown in the following figure:

The file application.conf is used to integrate TheHive with Cortex and MISP. You can learn how to set up the integration with Cortex  or here (TheHive documentation), while for the integration with MISP you can go  or here (TheHive documentation).
The URLs at which TheHive, Cortex and MISP instances are reachable should also be replaced in the file templates/index.html so that the buttons on the web interface will be able to reach them. To do that, replace the last three href of this portion of code:
<ul class=\"navbar-nav text-light\" id=\"accordionSidebar\">
    <li class=\"nav-item\"><a class=\"nav-link active\" href=\"/\" style=\"max-width: 114px;\" target=\"_blank\" rel=\"noopener noreferrer\"><img class=\"img-fluid\" data-bss-hover-animate=\"bounce\" src=\"../static/assets/img/logo_rounded.png\" style=\"margin-top: 0px;margin-left: 0px;\"></a></li>
    <li class=\"nav-item\"><a class=\"nav-link\" href=\"http://thehive:9000\" style=\"max-width: 114px;\" target=\"_blank\" rel=\"noopener noreferrer\"><img class=\"img-fluid\" data-bss-hover-animate=\"bounce\" src=\"../static/assets/img/thehive.png\" style=\"margin-right: 0px;margin-left: 0px;\"></a></li>
    <li class=\"nav-item\"><a class=\"nav-link\" href=\"http://cortex:9001\" style=\"max-width: 114px;\" target=\"_blank\" rel=\"noopener noreferrer\"><img class=\"img-fluid\" data-bss-hover-animate=\"bounce\" src=\"../static/assets/img/cortex.png\" style=\"transform: translate(0px);\"></a></li>
    <li class=\"nav-item\"><a class=\"nav-link\" href=\"https://misp\" style=\"max-width: 114px;\" target=\"_blank\" rel=\"noopener noreferrer\"><img class=\"img-fluid\" data-bss-hover-animate=\"bounce\" src=\"../static/assets/img/misp.png\" style=\"transform: translate(0px);\"></a></li>
</ul>
"
external_category: "Web Exploitation"
---[Visit Website](https://github.com/emalderson/ThePhish/tree/master/docker#configure-the-thehive-container)

