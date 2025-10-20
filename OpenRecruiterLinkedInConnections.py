import webbrowser
import time

# --- Configuration ---
# You can change this to 'firefox', 'safari', etc., if you are using a different browser.
# For Chrome, simply using `webbrowser.open_new_tab` often works without specifying the browser.
# If you run into issues, you may need to specify the path to your Chrome executable.
BROWSER_NAME = 'chrome' 

# List of all LinkedIn URLs provided by the user
LINKEDIN_URLS = [
    "https://www.linkedin.com/in/rojeethakur",
    "https://www.linkedin.com/in/anuradha-arora-18a4315",
    "https://www.linkedin.com/in/likhit-hs-128226163/",
    "https://www.linkedin.com/in/amali-khanna-1bb941a0",
    "https://www.linkedin.com/in/kanikasargoch/",
    "https://www.linkedin.com/in/pallavi-banerjee-59a0b019",
    "https://www.linkedin.com/in/nikhita-singh-a8423878",
    "https://www.linkedin.com/in/jaweria-zeya-658872117/",
    "https://www.linkedin.com/in/rishika-gowda-3ab451209/",
    "https://www.linkedin.com/in/richa-gautam-658676180/",
    "https://www.linkedin.com/in/hansa-punjabi-jha-6b5b94288/",
    "https://www.linkedin.com/in/lucy-deletta-062234154/",
    "https://www.linkedin.com/in/akhil-tajo-57a152117",
    "https://www.linkedin.com/in/bijish-menon-a74ba824",
    "https://www.linkedin.com/in/himanshu-ojha-637a232",
    "https://www.linkedin.com/in/anuraag-tapkir-0271783a",
    "https://www.linkedin.com/in/ajanta-anindita-b1a53120",
    "https://www.linkedin.com/in/megha-awasthi/",
    "https://www.linkedin.com/in/namratasen/",
    "https://www.linkedin.com/in/arunkakatkar/",
    "https://www.linkedin.com/in/chondu-chengappa-she-her-4ab98a5",
    "https://www.linkedin.com/in/jhumur-thakur-832a299",
    "https://www.linkedin.com/in/anusha-mittal-baa39b25",
    "https://www.linkedin.com/in/nayana-kumar-27b1233b",
    "https://www.linkedin.com/in/daryl-pinto-599b767",
    "https://www.linkedin.com/in/shivaniganjoo",
    "https://www.linkedin.com/in/renusd",
    "https://www.linkedin.com/in/prerna-gera",
    "https://www.linkedin.com/in/prasun-saxena-0969818/",
    "https://www.linkedin.com/in/pallavee-kumar-b8330613/",
    "https://www.linkedin.com/in/tara-raghuraman-a02657/",
    "https://www.linkedin.com/in/akhil-ravipalli/",
    "https://www.linkedin.com/in/divyabhurangi",
    "https://www.linkedin.com/in/goldy-sachdev-5a5b79114",
    "https://www.linkedin.com/in/himanshi-singhal-b91343137/",
    "https://www.linkedin.com/in/nitesh-kumar-64b39a69/",
    "https://www.linkedin.com/in/sneha-sharad-54266718/",
    "https://www.linkedin.com/in/prachi-parija-79968661/",
    "https://www.linkedin.com/in/nisha-rao-a8958832/",


    "https://www.linkedin.com/in/shrutygupta",
    "https://www.linkedin.com/in/pranav1991",
    "https://www.linkedin.com/in/rishi-wadehra-32633829",
    "https://www.linkedin.com/in/minothomas",
    "https://www.linkedin.com/in/mithun-jagadev-67473b5",
    "https://www.linkedin.com/in/swetha-pampati-8b3a8443/",
    "https://www.linkedin.com/in/ppriyanka233/",
    "https://www.linkedin.com/in/nikhil-dang-6791b3b1/",
    "https://www.linkedin.com/in/sujatha-devaraya-32640418/",
    "https://www.linkedin.com/in/vinayaka-db-8895a286/",
    "https://www.linkedin.com/in/suhail-khan-183099143/",
    "https://www.linkedin.com/in/nandini-shetty-b5023520/",
    "https://www.linkedin.com/in/tushali-paliwal/",
    "https://www.linkedin.com/in/pallabi-baruah-b6a67684/",
    "https://www.linkedin.com/in/ragini-madeshia-611412103/",
    "https://www.linkedin.com/in/rumana-khan-91181718",
    "https://www.linkedin.com/in/debasish1",
    "https://www.linkedin.com/in/mahiee-talreja-88965933",
    "https://www.linkedin.com/in/romeena-thomas",
    "https://www.linkedin.com/in/vidhyaag",
    "https://www.linkedin.com/in/jaisree-manoharan-379b7a22/",
    "https://www.linkedin.com/in/jennita-nanwani-7127b720/",
    "https://www.linkedin.com/in/anil-bhojwani/",
    "https://www.linkedin.com/in/rehan-akbar-5294394/",
    "https://www.linkedin.com/in/sanchita-gupta-340b82100/",
    "https://www.linkedin.com/in/pathanjali-bhat-53283225/",
    "https://www.linkedin.com/in/sailasri-sankaranarayanan-971229a0/",
    "https://www.linkedin.com/in/abhishek-barik-5a69bbb2/",
    "https://www.linkedin.com/in/sita-patel-a81a2496/",
    "https://www.linkedin.com/in/kalpanasampathkumar/",
    "https://www.linkedin.com/in/disha-dangi-66a9309b/",
    "https://www.linkedin.com/in/dhanush-mohan-b66b5267/",
    "https://www.linkedin.com/in/sandhya-rao-86a3b062/",
    "https://www.linkedin.com/in/pallabi-gochhi/",
    "https://www.linkedin.com/in/neahat91/",
    "https://www.linkedin.com/in/tiwarianamika/",
    "https://www.linkedin.com/in/soumya-naidu-33828419/",
    "https://www.linkedin.com/in/kiran-dawale-3ba8b572/",
    "https://www.linkedin.com/in/sunil610/",
    "https://www.linkedin.com/in/samir-roychowdhury-38b342103/",
    "https://www.linkedin.com/in/bharadwaj-vittala-b4460618",
    "https://www.linkedin.com/in/arun-p-sarma-b8ab06193/",
    "https://www.linkedin.com/in/shwetha-dsouza-14596355/",
    "https://www.linkedin.com/in/smriti-pandey-135b9915b/",
    
    
    "https://www.linkedin.com/in/balaji-chinni-8a3b1817b/",
    "https://www.linkedin.com/in/sonali-agarwal-5a3126193/",
    "https://www.linkedin.com/in/saima-jamal-61b578183/",
    "https://www.linkedin.com/in/shabeena-khatoon-37b060b7/",
    "https://www.linkedin.com/in/abhilashchipkar",
    "https://www.linkedin.com/in/irenepanicker",
    "https://www.linkedin.com/in/rosemarymathew",
    "https://www.linkedin.com/in/advithidilip",
    "https://www.linkedin.com/in/jyoti-bisht-7a120360",
    "https://www.linkedin.com/in/dorette-kuriachan-87b17739",
    "https://www.linkedin.com/in/nidhi-kumari-649069250",
    "https://www.linkedin.com/in/adarsh-ramakrishnappa-437b22205/",
    "https://www.linkedin.com/in/pragya-jalan-61b34128/",
    "https://www.linkedin.com/in/natraj-baskar-17165727/",
    "https://www.linkedin.com/in/vijay-balaji-42aa2b104/",
    "https://www.linkedin.com/in/jevitha-satya-b7a027181/",
    "https://www.linkedin.com/in/blessy-hannah-j-21b981181/",
    "https://www.linkedin.com/in/gayathri-venkat-554654a6/",
    "https://www.linkedin.com/in/jaya-subramanian",
    "https://www.linkedin.com/in/selvakumar-mohan-19047aa",
    "https://www.linkedin.com/in/siddarth-mohan-j-97989a17",
    "https://www.linkedin.com/in/srikanth-ganesan-536b106",
    "https://www.linkedin.com/in/anand-sankaran-b8723021",
    "https://www.linkedin.com/in/sumitpremi",
    "https://www.linkedin.com/in/sailaja-devendran-3b051a23",
    "https://www.linkedin.com/in/trisha-arya-0274a425",
    "https://www.linkedin.com/in/sonal-chotrani-0b6b32a3",
    "https://www.linkedin.com/in/chayanika-khakhlari-2a6114169",
    "https://www.linkedin.com/in/snehabathwal",
    "https://www.linkedin.com/in/vaibhav-goel-7631227",
    "https://www.linkedin.com/in/kritika-jain-50763759",
    "https://www.linkedin.com/in/praveenadevagupta",
    "https://www.linkedin.com/in/itsmadhumita",
    "https://www.linkedin.com/in/sharath-kumar-54226a29",
    "https://www.linkedin.com/in/arshrachit",
    "https://www.linkedin.com/in/komalsharma6",
    "https://www.linkedin.com/in/titash-paul-937358167"


]

def open_links_in_browser(urls, browser_name='chrome'):
    """
    Opens a list of URLs in new tabs in the specified web browser.

    Args:
        urls (list): A list of URL strings.
        browser_name (str): The name of the browser to use (e.g., 'chrome').
    """
    print(f"Attempting to open {len(urls)} links in {browser_name}...")
    
    # Try to get the browser controller
    try:
        browser = webbrowser.get(browser_name)
    except webbrowser.Error:
        print(f"Warning: Could not find '{browser_name}'. Falling back to default browser.")
        browser = webbrowser
        
    for i, url in enumerate(urls):
        try:
            # open_new_tab() attempts to open the URL in a new browser tab.
            browser.open_new_tab(url)
            print(f"Opened link {i+1}/{len(urls)}: {url}")
            
            # Pause for a short time to prevent the browser from being overwhelmed 
            # and to give LinkedIn time to load before the next tab opens.
            time.sleep(0.5) 
            
        except Exception as e:
            print(f"Error opening {url}: {e}")

if __name__ == "__main__":
    # Call the function to open all the links
    open_links_in_browser(LINKEDIN_URLS, BROWSER_NAME)
    print("\nScript execution finished. Check your browser for the new tabs.")
