import csv
import re

def process_athlete_data(file_path):

   # Extracting athlete stats by year
   records = []

   # Extracting athlete races
   races = []           

   athlete_name = ""
   athlete_id = ""
   comments = ""

   with open(file_path, newline='', encoding='utf-8') as file:
      reader = csv.reader(file)
      data = list(reader)

      athlete_name = data[0][0]
      athlete_id = data[1][0]
      print(f"The athlete id for {athlete_name} is {athlete_id}")

      for row in data[5:-1]:
         if row[2]:
            records.append({"year": row[2], "sr": row[3]})
         else:
            races.append({
               "finish": row[1],
               "time": row[3],
               "meet": row[5],
               "url": row[6],
               "comments": row[7]
            })

   return {
      "name": athlete_name,
      "athlete_id": athlete_id,
      "season_records": records,
      "race_results": races,
      "comments": comments
   }    

# def parse_time(time_str):
#    # remove non-numeric chars
#    if not time_str:
#       return 0
#    clean_time_str = re.sub(r"[^\d:.]", "", time_str)
#    parts = clean_time_str.split(':')
#    #if len(parts) == 2:
#    return int(parts[0]) * 60 + float(parts[1])
#    #return float(parts[0])

def gen_athlete_page(data, outfile):
   # template 
   # Start building the HTML structure
   # best_time = min(parse_time(race["time"]) for race in data["race_results"] if race["time"])
   html_content = f'''<!DOCTYPE html>
   <html lang="en">
   <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <!-- Get your own FontAwesome ID -->
       <script src="https://kit.fontawesome.com/ecb3a66f9b.js" crossorigin="anonymous"></script>
     
      <link rel = "stylesheet" href = "../css/style.css">
      

      <title>{data["name"]}</title>
   </head>
   <body>
   <a href = "#main">Skip to Main Content</a>
   <nav>
      <button class="nav-toggle" aria-label="Toggle navigation" onclick="toggleNavMenu()">☰ Menu</button>
      <ul class="nav-menu">
         <li><a href="../index.html">Home Page</a></li>
         <li><a href="../mens.html">Men's Team</a></li>
         <li><a href="../womens.html">Women's Team</a></li>
         <li><a href="#athlete-sr-table">Seasonal Records</a></li>
         <li><a href="#athlete-result-table">Race Results</a></li>
         <li><a href="#gallery">Gallery</a></li>
         <li><button onclick="setTheme('normal')">Normal Mode</button></li>
         <li><button onclick="setTheme('dark')">Dark Mode</button></li>
         <li><button onclick="setTheme('high-contrast')">High Contrast</button></li>
      </ul>
   </nav>
   <header>
      <!--Athlete would input headshot-->
       <h1>{data["name"]}</h1>
      
   </header>
      <img src="../images/profiles/{data["athlete_id"]}.jpg" alt="Athlete headshot" class="athlete-img"> 

   <main id = "main">
      <section id= "athlete-sr-table">
         <h2>Athlete's Seasonal Records (SR) per Year</h2>
            <table>
                  <thead>
                     <tr>
                        <th> Year </th>
                        <th> Season Record (SR)</th>
                     </tr>
                  </thead>
                  <tbody>
                  '''
   
   for sr in data["season_records"]:
      sr_row = f'''
                     <tr>
                        <td>{sr["year"]}</td>
                        <td>{sr["sr"]}</td>
                     </tr>                  
               '''
      html_content += sr_row

   html_content += '''                   
                </tbody>
                  </table>
                     </section>

                        <h2>Race Results</h2>

                        <section id="athlete-result-table">
                           

                           <table id="athlete-table">
                              <thead>
                                 <tr>
                                    <th><i class = "fa fa-person-running" aria-hidden="true"></i>Race</th>
                                    <th><i class="fa fa-clock" aria-hidden="true"></i>Athlete Time</th>
                                    <th><i class = "fa fa-medal" aria-hidden="true"></i>Athlete Place</th>
                                    <th><i class = "fa fa-message" aria-hidden="true"></i>Race Comments</th>
                                 </tr>
                              </thead>

                              <tbody>
                  '''
   
   # add each race as a row into the race table 
   for race in data["race_results"]:
      #race_time = parse_time(race["time"])
      #progress_width = (best_time / race_time) * 100 if race_time> 0 else 0
      race_row = f'''
                                 <tr class="result-row">
                                    <td>
                                       <a href="{race["url"]}">{race["meet"]}</a>
                                    </td>
                                    <td>{race["time"]}</td>
                                    <td>{race["finish"]}</td>
                                    <td>
                                       <button class="collapse-btn" onclick="toggleComments(this)">Show Comments</button>
                                       <div class="comment-content">{race["comments"]}</div>
                                    </td>
                                 </tr>
      '''
      html_content += race_row

   html_content += '''
                              </tbody>

                        </table>
                     </section>
                     <section id = "gallery">
                     <h2>Gallery</h2>
                      </section>
                     </main>
                     <footer>
                     <p>
                     Skyline High School<br>
                     <address>
                     2552 North Maple Road<br>
                     Ann Arbor, MI 48103<br><br>

                     <a href = "https://sites.google.com/aaps.k12.mi.us/skylinecrosscountry2021/home">XC Skyline Page</a><br>
                    <!--  Follow us on Instagram <a href = "https://www.instagram.com/a2skylinexc/"><i class="fa-brands fa-instagram" aria-label="Instagram"></i>  </a> -->

                     </footer>
               </body>
            
            <script>
               function toggleComments(button) {
                  const commentSection = button.nextElementSibling;
                  if (commentSection.style.display === "none" || commentSection.style.display === "") {
                     commentSection.style.display = "block";
                    button.textContent = "Hide Comments";
                  } else {
                     commentSection.style.display = "none";
                     button.textContent = "Show Comments";
                  }
               }

               function setTheme(mode) {
                  // Remove any existing theme classes
                  document.body.classList.remove('dark-mode', 'high-contrast-mode');

                  // Apply the chosen theme
                  if (mode === 'dark') {
                     document.body.classList.add('dark-mode');
                  } else if (mode === 'high-contrast') {
                     document.body.classList.add('high-contrast-mode');
                  }
               }

               function toggleNavMenu() {
                  const navMenu = document.querySelector('.nav-menu');
                  navMenu.classList.toggle('active');
               }
            </script>
         </html>
   '''

   with open(outfile, 'w') as output:
      output.write(html_content)


def main():

   import os
   import glob

   # Define the folder path
   folder_path = 'mens_team/'
   # Get all csv files in the folder
   csv_files = glob.glob(os.path.join(folder_path, '*.csv'))

   # Extract just the file names (without the full path)
   csv_file_names = [os.path.basename(file) for file in csv_files]

   # Output the list of CSV file names
   print(csv_file_names)
   for file in csv_file_names:

      # read data from file
      athlete_data = process_athlete_data("mens_team/"+file)
      # using data to generate templated athlete page
      gen_athlete_page(athlete_data, "mens_team/"+file.replace(".csv",".html"))

      # read data from file
      # athlete_data2 = process_athlete_data(filename2)
      # using data to generate templated athlete page
      # gen_athlete_page(athlete_data2, "enshu_kuan.html")


   # Define the folder path
   folder_path = 'womens_team/'
   # Get all csv files in the folder
   csv_files = glob.glob(os.path.join(folder_path, '*.csv'))

   # Extract just the file names (without the full path)
   csv_file_names = [os.path.basename(file) for file in csv_files]

   # Output the list of CSV file names
   print(csv_file_names)
   for file in csv_file_names:

      # read data from file
      athlete_data = process_athlete_data("womens_team/"+file)
      # using data to generate templated athlete page
      gen_athlete_page(athlete_data, "womens_team/"+file.replace(".csv",".html"))

      # read data from file
      # athlete_data2 = process_athlete_data(filename2)
      # using data to generate templated athlete page
      # gen_athlete_page(athlete_data2, "enshu_kuan.html")

if __name__ == '__main__':
    main()
