#Utility tools using Python

##Carmax Scrubber: 
1. Uses Python2.7
2. Automatically creates a csv file with needed data. The Scrubber is to scrub the store details in each city and state.

##VIN Decoder API:
1. User Python3.5
2. Consist of 3 file
  1. csv_reader_processor.py
  2. connect_api.py
  3. reaponse_xml_processor.py
3. csv_reader_processor is the main function. It reads the CSV file for VIN Numbers and connects with the API to extract the make, model and year of that vehicle. The details are then recorded on a separate CSV.
4. Place the csv file containing the vin numbers in the same location as the csv_reader_processor and rename it to 'sample_file.csv'. The vin numbers should be the first column in that file. Once processed, it will create another csv by name 'vin_details.csv' in the same location. The sample csv files have also been placed in repository for your reference. 

##General Instruction to run Python code:
1. Navigate to the respective main function location.
2. execute the below command
  1. python .\<file_name>.py
  
  
  
#Thanks for using my Code.
