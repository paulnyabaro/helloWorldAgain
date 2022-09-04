import traceback
try:
    raise Exception('An error occurred')
except:
    errorFile = open('errorLog.txt', 'a')
    print(errorFile.write(traceback.format_exc()))
    errorFile.close()
    print('The traceback info was written to errorLog')
