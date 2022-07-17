import speedtest

test = speedtest.Speedtest()
print("loading server list...")
test.get_servers()
print("choosing best server...")
best_server = test.get_best_server()
print("server connected!")
print(f"Location: {best_server['name']}{str(',')}{best_server['country']} |Sponsor: {best_server['sponsor']}"
      f" |Host: {best_server['host']}")
print("speed analyzing...")
downloading = test.download()
uploading = test.upload()


print(f"Downloading Speed:{downloading/1024/1024:.2f} mbps")
print(f"Uploading Speed:{uploading/1024/1024:.2f} mbps")
