## GloPAD - retirement planning

* updated - jgr25@cornell.edu - 8/16/2016

### Summary
GloPAD is a grant funded web application written by CUL 2002-2009. The application has a lot of web security problems. Library Systems has applied mod_security as a temporary blanket fix for the issues. This breaks a lot of the application's functions. The problem at hand is how to maintain availability the information in the site, while avoiding the security issues.

### Scope

* This is not intended as a proposal, just a document describing the current state of GloPAD (as of Aug 2016).
* Work in progress, not complete
* I will try to keep the detailed information in separate documents

### What is GloPAD

* From GloPAC
  > GloPAD is a multimedia, multilingual, Web-accessible database containing digital images, texts, video clips, sound recordings, and complex media objects (such as 3-D images) related to the performing arts from around the world.
* GloPAD is a custom built web application written in php with a postgres database back end. There is a [Public Interface (pi)](http://www.glopad.org/pi/) for users to search and browse, and an [Editor Interface (ei)](http://www.glopad.org/ei/) for data entry and editing, and an [online help system](http://www.glopac.org/exported_help/glopad_ei_help.htm) for the Editors
* Metadata Information - [GloPAD Metadata Standards](http://www.glopac.org/about/aboutMetadata.php)

### Who uses GloPAD

* Web hit counts (PIWIK)
  * 2016 - 54,098 visits; 361,492 pageviews (non _js version)
  * 2015 - 93,067 visits; 415,943 pageviews
* Research
* Associated applications
  * [JPARC](http://www.glopad.org/jparc/) - uses glopad apis for some of it's data. It is a Drupal 5 application. GloPAC is working on a Drupal 7 version of JPARC.

### Current state of GloPAD

* Security problems
  >The AppSpider scan completed, and found 77 high-level vulnerabilities (a mixture of SQL injection and local file inclusion) out of a total of 870 issues.
  -Chris Manly

   * According to AppSpiderEnterprise, it would take an Application Developer an estimated 579 man hours, and a Database Administrator an estimated 67 man hours to fix the issues.
* Web services in use
* Object counts
  * see object_counts.md
* Functions broken in current application
  * OAI harvesting
  * the main custom search function, for both the public interface and the editors’ interface
     * [GloPAD Records Text Search](http://www.glopad.org/pi/en/search_browse.php) does work for pi only
  * the record create and update functionality on the editors’ interface

### Stakeholders

* CUL
* CUL-IT
* CUL Library Systems
* GloPAC - Global Performing Arts Consortium - [About GloPAC] (http://www.glopac.org/about/index.php)
* Mario Einaudi Center for International Studies [East Asia Program](https://eap.einaudi.cornell.edu/)
* Josh Young, principal investigator and [East Asia Program Manager](https://eap.einaudi.cornell.edu/person/joshua-young)
* Mai Shaikhanuar-Cota, the [Cornell East Asia Series Managing Editor](https://eap.einaudi.cornell.edu/person/mai-shaikhanuar-cota)


### Issues

* Funding
* Ownership
* Responsibility for preservation
* Utility
* Value of the collection
* Security Vulnerabilities

### Opinions

Stakeholder's opinion on each issue
