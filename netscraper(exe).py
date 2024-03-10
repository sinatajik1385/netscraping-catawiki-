import threading
import subprocess
import time
def find_gems () :
    def run_script(script_name):
        subprocess.run(["python", script_name])

    if __name__ == "__main__":
        script1_thread = threading.Thread(target=run_script, args=("project/netscraper_catawiki_emeralds.py",))
        script2_thread = threading.Thread(target=run_script, args=("project/netscraper_catawiki_garnets.py",))
        script3_thread = threading.Thread(target=run_script, args=("project/netscraper_catawiki_hessonites.py",))
        script4_thread = threading.Thread(target=run_script, args=("project/netscraper_catawiki_opal.py",))
        script5_thread = threading.Thread(target=run_script, args=("project/netscraper_catawiki_rubies.py",))
        script6_thread = threading.Thread(target=run_script, args=("project/netscraper_catawiki_saphires.py",))
        script7_thread = threading.Thread(target=run_script, args=("project/netscraper_catawiki_spinels.py",))
        script8_thread = threading.Thread(target=run_script, args=("project/netscraper_catawiki_tanzanites.py",))



        script1_thread.start()
        script2_thread.start()
        script3_thread.start()
        script4_thread.start()
        script5_thread.start()
        script6_thread.start()
        script7_thread.start()
        script8_thread.start()

        script1_thread.join()
        script2_thread.join()
        script3_thread.join()
        script4_thread.join()
        script5_thread.join()
        script6_thread.join()
        script7_thread.join()
        script8_thread.join()

        print("a scripts have finished executing.")
if __name__ == "__main__" :
    while True :
        find_gems()
        time_wait = 30
        print (f'waiting {time_wait} minuts')
        time.sleep (time_wait *60)