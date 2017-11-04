# ML1 - Problem Sheet 1

## Problem 1a and 1b

### Sentiment Analysis

Given an input in text- or audio-format, the goal is to identify the sentiment of the author, e.g. whether he's angry or happy.
The inputs are content in written text or spoken audio format, possibly together with meta-information such as author data (age, profession) or information concerning the retrieval of the data itself like the platform / channel it was obtained from (Twitter, Blogs, Survey) or date/time it was recorded.
The label is one of many (typically 2: good / bad) predefined states the subject may be in, such as angry, scared, happy, adventurous. 

Intuitively, humans are good at judging content like choice of words, body-language or intonation to a persons sentiment, but hard-coded rules are much more difficult for computers to generate and adapt. The aspect of typical human interaction and inferring sentiment from a given situation is hard for computers as they do not natively understand "typical" human behavior. 

### Author Influence

Given (social media) data of multiple sources structured by author / publisher of the information, the goal is to identify key figures of influence in a given network of information.
The inputs are data metrics to published articles, research, appearing and connections to an identities public appearance. This may also take into account meta-information like covariance to other identities and their metrics or association with a predefined group of typically influential identities.
The labels are typically a numeric value (hence appliance of regression rather than classification) indicating overall influence. This number may also be broken down to influence on a specified sub-group divided by age / interests / marketing potential / ... .  

Author influence is a rather complex topic for us humans, too. We generally understand which figure has a major influence on which area of interest, like which musician will reach most people may be easily deduced e.g. by how frequently said musician appears on local radio. But braking it down to an accurate ranking amongst many individuals concerning a multitude of fields to estimate influence upon is a process of highest-order number crunching and statistics, at which a computer naturally excels.

### Malicious Network Traffic Detection

Machine Learning is also used for security purposes. As such, it was e.g. used for learning what kind of network traffic was to be expected by a given to-be-supervised network. In the case of an initiated attack on the network or immediate leaking of data from within, this could be then detected as an abnormal behavior to proclaim that "the network's security was compromised".
For input, the data traffic (size, frequency, table of recipients, ...) is monitored and metrics learned and foreshadowed.
The labels would be a numeric estimation of "normal behavior", to which a threshold should be applied to create some buffer for "different, yet still ordinary" behavior. As the numeric estimation regresses to unexpected values, alarm is being thrown.
This all may also incorporate associate rule learning to draw direct connections to which sequence of connected actions should result in alarms being thrown and which ones should not.

Detecting malicious behavior of a network involves keeping track of a multitude of logs, network traffic, health-checks and more. A system-administrator knows a plethora of tools and software to help keeping track of all of this information, but an automated system (if it is able to properly map all dependent systems) can more easily draw non-intuitive connections and is needed to cover the ever-growing complexity and scope of systems at hand. 


## Problem 1c

Find 2-3 AI/ML companies in Kaiserslautern and give a short description of them.

### Insiders

It was founded in 1998, has around 100 employees and its headquarter in Kaiserslautern (with another seat in Berlin).
[Homepage](https://www.insiders-technologies.de/home.html)

Insiders Technology specializes on AI for understanding documents. Intelligent software solutions are applied to business processes to optimize business insights and streamline reporting. Its overall goal is to orchestrate a businesses digital transformation with respect to automation, customer relation and general information management.
Its offerings include *Input Management* (digital mailroom, billing service, order management), *Customer Communication* (Customer engagement platform, response management, process transparency), *Mobile* (chat / capture / info / contracts / services applications), *Cloud* (IT-Infrastructure offerings, scalable (Web-)services) and *Business Intelligence* (engaging business processes, service quality assurance, forecasting; connected to the *digital mailroom*-offering).

### Deutsches Forschungszentrum für Künstliche Intelligenz (DFKI)

Seated at Kaiserslautern, Saarbrücken (Headquarter), Bremen, Berlin (project bureau) and with an associated branch in Osnabrück, the DFKI presents itself as a "Center of Excellence" and one of the biggest research centers surrounding the field of Artificial Intelligence. It was founded in 1988 and is a non-profit with around 300 employees.

The DFKI focuses on AI research and appliance of related technology. To name some specific focus points, it structures its areas of research, research groups and living labs as follows: Smart Data, Cyber-Physical systems, multilingual technology, plan-based robot control,  educational tech., interactive fabric, innovative retail, business informatics, embedded intelligence, smart service engineering, intelligent large-scale analytics, innovative industrial systems, intelligent networks, augmented reality, speech technology and intelligent interfaces.
It also focuses on a tight incorporation of the respective location's focus in research to draw local expertise into the equation.

## Problem 1d

[...]

## Problem 2

_Question_:

- Play around with the MNIST dataset
- get farmiliar with kaggle, kaggle challenge !

[...]