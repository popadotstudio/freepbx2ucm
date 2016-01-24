ucm_versions = {
	"UCM6510": ["1.0.2.5"],
	"UCM61xx": ["1.0.9.25"],
}

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


# REQUIRED Options, already included in the above default template

# "Strategy" = "Allow All"
# "Skip Voicemail Password Verification" = "yes" # yes (no)
# "Technology" = "SIP"
# "Auto Record" = "no" # no (yes)
# "SRTP" = "no" # no (yes)
# "Skip Trunk Auth" = "no" # no (yes)
# "Codec Preference" = "PCMU,PCMA,GSM,G.726,G.722,G.729,H.264,ILBC"
# "Permission" = "Internal"
# "NAT" = "yes" # yes (no)
# "Can Reinvite" = "no" # no (yes)
# "Insecure" = "Port"
# "Enable Keep Alive" = "no" # no (yes)
# "Keep Alive Frequency" = "60"
# "Support Hot Desking Mode" = "no" # no (yes)
# "Disable This Extension" = "no" # no (yes)
# "Music On Hold" = "default"
# "CC Agent Policy" = "never"
# "CC Monitor Policy" = "never"