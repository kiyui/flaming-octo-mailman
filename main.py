#!/usr/bin/env python3
import argparse, json
from urllib.request import urlopen
from urllib.parse import urlencode

'''
Class that converts a JSON file
into a list of dictionaries.
'''
class POSTData:
    def __init__(self, fileDir):
        self.fileDir = fileDir
        with open(self.fileDir, 'r') as jsonData:
            self.fileData = json.load(jsonData)

    def get(self):
        return self.fileData

def main(args):
    # Get command line arguments
    arg_url = args.url
    arg_file = args.file
    arg_save = args.save
    arg_noredirect = args.noredirect
    arg_success = args.noretry
    arg_verbose = args.verbose
    arg_silent = args.silent
 
    # Create POST data
    try:
        formData = POSTData(arg_file)
    except:
        # Verbose logging
        if arg_verbose:
            print('POST data parsing failed')
        return 1
 
    # Verbose logging
    if arg_verbose:
        print('JSON data parsed:')
        for jsonData in formData.fileData:
            print(jsonData)
 
    # POST dictionary list
    dictList = formData.get()
    
    # Main program loop
    success = False
    while not success:
        try:
            # Access URL
            if arg_verbose:
                print('Attempting to connect')
            openURL = urlopen(arg_url)
                
            # Check if redirect occured
            if openURL.geturl() != arg_url:
                # Verbose logging
                if arg_verbose:
                    print('A redirect occured')
                if arg_noredirect:
                    if arg_verbose:
                        print('Not allowing redirect.')
                    continue

            # End loop cycle
            success = True

            # Verbose logging
            if arg_verbose:
                print('Successfully connected')
 
            # Send data
            for i in range(0, len(dictList)):
                # Verbose logging
                if arg_verbose:
                    print('Now sending:')
                    print(dictList[i])

                # Prepare to POST data
                dictPOST = urlencode(dictList[i])
                dictPOST = dictPOST.encode('utf-8')
                
                # Attempt POST
                openURL = urlopen(arg_url, dictPOST)
                
                # Print output
                readURL = openURL.read()
                readURL = readURL.decode('utf-8')
                if not arg_silent:
                    print(readURL)

                # Save data
                if arg_save:
                    with open('POSTReturn_' + str(i) + '.html', 'w') as returnData:
                        returnData.write(readURL)
                        returnData.close()

        except KeyboardInterrupt:
            print('Quit')
            return 1
        except:
            # Verbose logging
            if arg_verbose:
                print('Failed to open')
            
            # Check if we need to retry
            if arg_success:
                # Verbose logging
                if arg_verbose:
                    print('Not going to retry.')
                return 1
    return 0

if __name__ == '__main__':
    # Create arguments
    parser = argparse.ArgumentParser(description='Sends formatted POST data from a file to a URL')
    parser.add_argument('-u', '--url', help='URL to POST data', required=True)
    parser.add_argument('-f', '--file', help='POST file directory (JSON)', required=True)
    parser.add_argument('-s', '--save', help='Save POST output', action='store_true')
    parser.add_argument('-r', '--noredirect', help='Disable redirects', action='store_true')
    parser.add_argument('-n', '--noretry', help='Do not retry on failure', action='store_true')
    parser.add_argument('-x', '--silent', help='Do not print page', action='store_true')
    parser.add_argument('-v', '--verbose', help='Verbose logging', action='store_true')
    args = parser.parse_args()

    # Call main function
    quit(main(args))
