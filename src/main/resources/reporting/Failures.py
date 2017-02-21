#################################################################################################
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
###################################################################################################

totalFails = 0
currentPhaseFails = 0
for p in release.phases:
    for t in p.tasks:
        totalFails += t.failuresCount

cp = getCurrentPhase()
for t in cp.tasks:
    currentPhaseFails += t.failuresCount