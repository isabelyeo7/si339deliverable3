import os

def generate_mens_team_page():
    # Path to the women's team folder
    mens_team_folder = 'mens_team'
    mens_team_page = 'mens.html'

    # HTML structure for the women's team page
    html_content = '''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Women's Team</title>
        <link rel="stylesheet" href="css/style.css"> <!-- Link to your CSS file -->
    </head>
    <body>
        <header>
            <h1>Men's Team</h1>
            <p>Click on an athlete's name to view their profile.</p>
        </header>
        
        <main>
            <ul>
    '''

    # Loop through all HTML files in the women's team folder
    for filename in os.listdir(mens_team_folder):
        if filename.endswith('.html'):
            # Generate a link for each athlete's page
            athlete_name = filename.replace('.html', '').replace('_', ' ').title()
            athlete_name = athlete_name.translate(str.maketrans('', '', '0123456789'))
            html_content += f'<li><a href="{mens_team_folder}/{filename}">{athlete_name}</a></li>\n'

    # Complete the HTML structure
    html_content += '''
            </ul>
        </main>
        
        <footer>
            <p>&copy; 2024 Men's Team Profiles</p>
        </footer>
    </body>
    </html>
    '''

    # Write the generated HTML to the women's team page
    with open(mens_team_page, 'w') as file:
        file.write(html_content)

    print(f"{mens_team_page} has been generated successfully.")

# Run the function to generate the women's team page
generate_mens_team_page()