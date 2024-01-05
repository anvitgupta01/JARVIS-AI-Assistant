import speedtest

def speedTest() :
    st = speedtest.Speedtest()
    st.get_best_server()
    upload = st.upload()
    download = st.download()

    print(f"The upload speed is {upload/1_000_000}") # convert to mbps
    print(f"The download speed is {download/1_000_000}") # convert to mbps