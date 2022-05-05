import urllib.request, sys
print("- CONTENT OF "+sys.argv[1]+" -\r\n"+urllib.request.urlopen(sys.argv[1]).read().decode("utf8"))