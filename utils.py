import pymsgbox
def printVerification(isVerified):
    if isVerified:
        result = 'Accepted'
    else:
        result = 'Rejected'
    print(result)
    pymsgbox.alert(result, 'Result', timeout=3000)