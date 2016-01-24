# freepbx2ucm

**freepbx2ucm** converts (intelligently) between FreePBX's Bulk Extensions CSV format and the Grandstream's UCM series CSV format. It comes with a built-in template that maps FreePBX to the UCM's columns, while implementing logic to convert between the two different platforms. It has been tested on Grandstream's UCM6510 and pending other models for testing.

The idea behind this script was to ease the transition from FreePBX-based Asterisk PBX systems to the Grandstream UCM series PBXes. Unfortunately, because Grandstream software currently (Jan-2015) doesn't support a way to bulk import DIDs, the script is concerned only with extensions. Even still, a lot of people will appreciate its usefulness once your current PBX has over 100-200 extensions.

*Note: There is pending work on a DID bulk import, however that process will be slightly more involved*

##Installation with Binaries
Downloadable binaries for both Windows and Mac are available here:
[FreePBX to Grandstream UCM CSV Converter Windows/Mac Binaries - freepbx2ucm](http://northshoreit.me/freepbx-to-grandstream-ucm-freepbx2ucm/)
Simply download and extract the zip.

##Installation with PIP
The script is written in Python 3.5 (it could be ported to lower 3.x versions but there I see no reason for it currently).
Clone the repo and get started:
~~~
git clone https://github.com/veryxcit/freepbx2ucm.git
cd freepbx2ucm
pip install -r requirements.txt
~~~
---
##Quickstart
* Log into your favorite FreePBX based distro, and make sure you have the [Bulk Extensions](http://wiki.freepbx.org/display/FPG/Bulk+Extensions).
* Export your CSV and save it in the same dir as freepbx2ucm [here's a video I found](https://www.youtube.com/watch?v=TChvvUb7OPghttps://www.youtube.com/watch?v=TChvvUb7OPg).
* Type the following:
~~~
freepbx2ucm <bulkextensions_csv_file_goes_here>
~~~
* The script will export by default to "ucm_export.csv" in the same dir.
* Log into your Grandstream UCM, go to PBX, then Extensions, then import the file.
* Submit issues (and feature requeusts) [here](https://github.com/veryxcit/freepbx2ucm/issues) as this is in beta status.

##Slightly Advanced Usage

Once installed please review the CLI parameters with:
~~~
freepbx2ucm --help

Usage: freepbx2ucm.py [OPTIONS] FREEPBX_CSV [UCM_CSV_OUT]

  This script converts (intelligently) between FreePBX's Bulk Extensions CSV
  and the Grandstream's UCM series CSV. It comes with a built-in template
  that maps FreePBX to the UCM's columns, while implementing logic to
  convert between the two different platforms. It has been tested on
  Grandstream's UCM6510 and pending other models for testing.

  Arguments:
  FREEPBX_CSV is the INPUT CSV file and it is required
  UCM_CSV_OUT is the OUTPUT CSV file, by default it exports to "ucm_export.csv"

  Notes:
  - Only processes SIP and IAX extensions (should be more than enough).
  - Deals with password requirements (enforced by the UCM software) in an
    automatic and opinionated way, altough this can be altered via options.
  - The built-in template can be overridden to include additional parameters.

Options:
  --template PATH  Uses a custom template file. Copy "mappings.py" and edit
                   your own custom parameters.
  --bypasscount    Ignores failed import count check, make sure to visually
                   inspect the parsed data first.
  --allrandom      Instead of padding the existing passwords with 0's, random
                   passwords will be generated.
  --prettyname     Converts the extension name from e.g. FIRST LAST to First
                   Last
  --usefaxemail    FreePBX has email and faxemail, UCM only has email, this
                   option grabs faxemail if email doesn't exist
  --help           Show this message and exit.
~~~

##Template
The default template invoked by the script is "mappings.py". If you'd like to edit parameters for all generated extensions, this is the place to do it. You may also copy it and use the --template switch to use a different file. The default template covers a lot of ground and there is logic built-in to handle many inconsitencies.

Here are the default mappings and the logic behind them:
* extension (only accepts valid extension numbers, and only SIP and IAX types)
* SIP/IAX password (if password is under 4 characters, it pads the current password with 0's or generates a random password)
* voicemail (yes/no)
* voicemail password (if password is under 4 characters, it pads the current password with 0's or generates a random password)
* outbound caller ID (since FreePBX also includes a name in its outboundcid, we only parse the numbers)
* fax (yes/no)
* DTMF mode
* user password (generated automatically)
* first and last name (if name has 2 words in it e.g. John Smith, it will separate the two for the UCM, and there is a prettyfing flag)
* email (in FreePBX there are 2 separate ares for email and fax email, there is a flag that says grab from fax email, if email is blank)

##Copy And Paste Template
Here is the default template if you are too lazy to clone the repo:
~~~python
mappings_template = {
	"Extension"                                  : "{{ ucm.extension }}",
	"Technology"                                 : "SIP",
	"Enable Voicemail"                           : "{{ ucm.vm }}",
	"CallerID Number"                            : "{{ ucm.outcid }}",
	"SIP/IAX Password"                           : "{{ ucm.sip_pass }}",
	"Voicemail Password"                         : "{{ ucm.vm_pass }}",
	"Skip Voicemail Password Verification"       : "yes",
	"Ring Timeout"                               : "",
	"Auto Record"                                : "no",
	"SRTP"                                       : "no",
	"Fax Mode"                                   : "{{ ucm.fax }}",
	"Strategy"                                   : "Allow All",
	"Local Subnet 1"                             : "",
	"Local Subnet 2"                             : "",
	"Local Subnet 3"                             : "",
	"Local Subnet 4"                             : "",
	"Local Subnet 5"                             : "",
	"Local Subnet 6"                             : "",
	"Local Subnet 7"                             : "",
	"Local Subnet 8"                             : "",
	"Local Subnet 9"                             : "",
	"Local Subnet 10"                            : "",
	"Specific IP Address"                        : "",
	"Skip Trunk Auth"                            : "no",
	"Codec Preference"                           : "PCMU,PCMA,GSM,G.726,G.722,G.729,H.264,ILBC",
	"Permission"                                 : "Internal",
	"NAT"                                        : "yes",
	"Can Reinvite"                               : "no",
	"DTMF Mode"                                  : "{{ ucm.dtmf }}",
	"Insecure"                                   : "Port",
	"Enable Keep-alive"                          : "no",
	"Keep-alive Frequency"                       : "60",
	"AuthID"                                     : "",
	"TEL URI"                                    : "Disabled",
	"Call Forward Busy"                          : "",
	"Call Forward No Answer"                     : "",
	"Call Forward Unconditional"                 : "",
	"Support Hot-Desking Mode"                   : "no",
	"Dial Trunk Password"                        : "",
	"Disable This Extension"                     : "no",
	"CFU Time Condition"                         : "All Time",
	"CFN Time Condition"                         : "All Time",
	"CFB Time Condition"                         : "All Time",
	"Music On Hold"                              : "default",
	"CC Agent Policy"                            : "never",
	"CC Monitor Policy"                          : "never",
	"CCBS Available Timer"                       : "4800",
	"CCNR Available Timer"                       : "7200",
	"CC Offer Timer"                             : "60",
	"CC Max Agents"                              : "1",
	"CC Max Monitors"                            : "2",
	"Ring simultaneously"                        : "no",
	"External Number"                            : "",
	"Time Condition for Ring Simultaneously"     : "All Time",
	"Enable LDAP"                                : "yes",
	"User Password"                              : "{{ ucm.user_pass }}",
	"First Name"                                 : "{{ ucm.fname }}",
	"Last Name"                                  : "{{ ucm.lname }}",
	"Email Address"                              : "{{ ucm.email }}",
	"Language"                                   : "Default",
}

mappings_header = ["Extension", "Technology", "Enable Voicemail", "CallerID Number", "SIP/IAX Password", "Voicemail Password", "Skip Voicemail Password Verification", "Ring Timeout", "Auto Record", "SRTP", "Fax Mode", "Strategy", "Local Subnet 1", "Local Subnet 2", "Local Subnet 3", "Local Subnet 4", "Local Subnet 5", "Local Subnet 6", "Local Subnet 7", "Local Subnet 8", "Local Subnet 9", "Local Subnet 10", "Specific IP Address", "Skip Trunk Auth", "Codec Preference", "Permission", "NAT", "Can Reinvite", "DTMF Mode", "Insecure", "Enable Keep-alive", "Keep-alive Frequency", "AuthID", "TEL URI", "Call Forward Busy", "Call Forward No Answer", "Call Forward Unconditional", "Support Hot-Desking Mode", "Dial Trunk Password", "Disable This Extension", "CFU Time Condition", "CFN Time Condition", "CFB Time Condition", "Music On Hold", "CC Agent Policy", "CC Monitor Policy", "CCBS Available Timer", "CCNR Available Timer", "CC Offer Timer", "CC Max Agents", "CC Max Monitors", "Ring simultaneously", "External Number", "Time Condition for Ring Simultaneously", "Enable LDAP", "User Password", "First Name", "Last Name", "Email Address", "Language"]
~~~
