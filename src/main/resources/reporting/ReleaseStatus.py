#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#
outputString = ""
phase = getCurrentPhase()
release = getCurrentRelease()

outputString += "Release Title:"+str(release.title)
outputString += "\nRelease Owner:"+str(release.owner)
outputString += "\nRelease Id:"+str(release.id)
outputString += "\nRelease Status:"+str(release.status)
outputString += "\nPhase Title:"+ str(phase.title)
outputString += "\nPhase Id:"+str(phase.id)
outputString += "\nPhase Status:" +str(phase.status)
print(outputString)