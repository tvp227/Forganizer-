import os
import shutil

# Set the path to the Documents folder
documents_folder = os.path.join(os.path.expanduser("~"), "Documents")

# Specify the keywords to organize files
keyword_mappings = {
    'Invoice': 'Financial',
    'Receipt': 'Financial',
    'Payroll': 'Financial',
    'Resume': 'JobApplications',
    'Cover Letter': 'JobApplications',
    'CV': 'JobApplications',
    'Meeting': 'Meetings',
    'Project': 'Projects',
    'Proposal': 'Projects',
    'Task': 'Projects',
    'Presentation': 'Presentations',
    'Photo': 'Photos',
    'Vacation': 'Travel',
    'Flight': 'Travel',
    'Hotel': 'Travel',
    'Passport': 'Travel',
    'Contract': 'Legal',
    'Agreement': 'Legal',
    'License': 'Legal',
    'Policy': 'Legal',
    'Report': 'Reports',
    'Analysis': 'Reports',
    'Survey': 'Reports',
    'Manual': 'Manuals',
    'Guide': 'Manuals',
    'GameSave': 'GameSaves',
    'SaveFile': 'GameSaves',
    'SaveData': 'GameSaves',
    'EML': 'Emails',
    'Email': 'Emails',
    'Playbook': 'SentinelDeployments',
    'Analytic Rules': 'SentinelDeployments',
    'Workbook': 'SentinelDeployments',
    'Training': 'Education',
    'Certificate': 'Education',
    'Course': 'Education',
    # Add more keywords and corresponding folder names as needed
}

# Function to organize files based on keywords
def organize_files(source_path, destination_path):
    # Ensure the source path is the default Documents folder
    if source_path.lower() != documents_folder.lower():
        print("Error: The source path is not the default Documents folder.")
        return

    # Get all files in the source directory
    files = os.listdir(source_path)

    # Report to store the results
    report = {'Moved': [], 'NotMoved': []}

    # Organize files based on keywords
    for file_name in files:
        moved = False
        for keyword, folder in keyword_mappings.items():
            if keyword.lower() in file_name.lower():
                # Ensure the destination folder exists before moving
                destination_folder = os.path.join(destination_path, folder)
                os.makedirs(destination_folder, exist_ok=True)
                
                shutil.move(os.path.join(source_path, file_name), os.path.join(destination_folder, file_name))
                report['Moved'].append(file_name)
                moved = True
                break

        # If the file hasn't been moved, add to the report
        if not moved:
            report['NotMoved'].append(file_name)

    # Print the report
    print("Files successfully moved:")
    print("\n".join(report['Moved']))
    
    print("\nFiles not moved:")
    print("\n".join(report['NotMoved']))

# Call the function to organize files
organize_files(source_path=documents_folder, destination_path=documents_folder)
