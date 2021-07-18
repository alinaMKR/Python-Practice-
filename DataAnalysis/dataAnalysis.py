# import matplolib for graph
import matplotlib.pyplot as plt



#start main function
def main():

    #step1
    #call function to read files
    print ("--- STEP 1 ---")
    try:
        women_dic = read_file_dic("bmi_women.csv")
        men_dic = read_file_dic("bmi_men.csv")
        life_list = read_file_list("life.csv")
        print ("All files have been successuly read", '\n')
    except:
        print("Error occured while reading some of the files")

    #step2
    #create bmi_all dictionary
    print ("--- STEP 2 ---")
    try:
        create_bmi_all()
        print("New dictionary with Gender-aberage BMI data was created",'\n')
    except:
        print("Error occured while creating gender-average dictionary")

    #step3
    #compute statistics
    print ("--- STEP 3 ---")
    val = 0
    #set loop to countinue till valid input is taken
    while val ==0:
        try:
            #take input
            year = int(input("Select a year between 1980 and 2008 to display statistics: "))
            #call function
            find_statistics(year)
            val =1 #finish loop
        #except for invalid value of input
        except ValueError:
            print("Error: That is invalid year")
            val=0 #continue loop

    #step4
    #statistics of BMI men vs women
    print ("--- STEP 4 ---")
    print("Men vs women BMI in highest population countries:", '\n')
    men_vs_women()

    #step5
    #plot of life expectancy
    print ("--- STEP 5 ---")
    v=0
    while v==0:
        try:
            country = input("Enter the country to visualize life expectancy data: \n")
            life_data(country.lower())
            v=1
        except:
            print(country, "is invalid name")
            v=0

    #step6
    #plot of corralation between BMI and Life expectancy
    print ("--- STEP 6 ---")
    print("Correlation plot opens in a new window.", '\n')
    correlation()
    print ("Goodbye")



#define function to read file and create dictionary
def read_file_dic(file_path):
    #call try/except statement
    try:
        #open file for reading
        file_obj = open (file_path, "r")
    except IOError:
    #print IOerror message in case of wrong input
        print("Err: File was not found")

    #declare empty dictionary for data
    data_dic = {}
    #declare empty dictionary for header
    header_dic = {}
    #declare empty list for data
    list = []
    #declare empty list for header
    header_list = []
    #define counter
    counter = 0

    #start for loop for a number of lines
    for line in file_obj:
        #increase counter by one for each iteration
        counter +=1
        #condition for header
        if counter ==1:
            #seperate lines
            values = line.rstrip('\n')
            #split values with comma
            values = line.split(',')
            #identify value with 0 index as a key
            key = values[0]
            #identify values, starting with index 1, as set of data for header
            header_list = values[1::]
            header_float = [int(i) for i in header_list]
            header_dic[key] = header_float
        #condition for the rest of data
        else:
            #seperate lines
            values = line.rstrip('\n')
            #split values with comma
            values = line.split(',')
            #identify value with 0 index as a key
            key = values[0]
            #identify values, starting with index 1, as set of data for list
            list = values[1::]
            data_float = [float(i) for i in list]
            data_dic[key] = data_float

    #close file
    file_obj.close()
    #return results of dicitionary
    return header_dic, data_dic



#define function to read file and create 2d list
def read_file_list (file_path):
    try:
        #open file for reading
        file_obj = open (file_path, "r")
    except IOError:
    #print error message in case of wrong input
        print("Err: File was not found")

    ##create emply lists for data and headers
    new_list = []
    new_list_header = []

    #set counter
    counter = 0

    #start loop for each line of a file
    for line in file_obj:
        #increase counter by one for each iteration
        counter +=1
        #condition for header
        if counter ==1:
            values = line.strip('\n')
            values = line.split(',')
            new_list_header = values[:]
        #condition for the rest of data
        else:
            #attach every line as a new set of values to a list
            new_list.append(line.split(','))

    #close file
    file_obj.close()
    #return results of 2dlist
    return new_list_header, new_list


#define function to create average bmi_all dictionary
def create_bmi_all():
    #reference dictionaries
    bmi_men_header,bmi_men_data=read_file_dic("bmi_men.csv")
    bmi_women_header,bmi_women_data=read_file_dic("bmi_women.csv")

    #create bmi_all dictionary
    bmi_all={}
    bmi_list=[]
    #check for same key in men`s an women`s list
    for key in list(set(bmi_men_data)|set(bmi_women_data)):
        #get the keys if matched
        if bmi_men_data.get(key) and bmi_women_data.get(key):
            i=bmi_men_data.get(key)
            j=bmi_women_data.get(key)
            #create zipped list of men`s and women`s data
            combined_list=zip(i,j)
            #create a list of combined keys and average values
            bmi_list=[round((x+y)/2,2) for (x,y) in combined_list]
            #set key
            bmi_all[key]=bmi_list
            bmi_all_header = bmi_men_header
    return bmi_all_header, bmi_all


#define function to find statistics of spesific year
def find_statistics(year):
    #reference dictionary
    bmi_all_header, bmi_all = create_bmi_all()
    list = []
    list = bmi_all_header['country']
    #find index of entered year
    year_index = list.index(year)
    all_list = []
    year_list = []
    counter = 0
    total = 0
    min_value = 100
    max_value = 0
    counter_min = 0
    counter_max = 0
    c = 0
    for line in bmi_all:
        counter+=1
        all_list = bmi_all[line]
        #choose index of spesific year
        value = all_list[year_index]
        #create a list of values at that index
        year_list.append(value)
        #find minimum value
        if min_value >= value:
            min_value = value
            counter_min = counter
        #find maximum value
        if max_value < value:
            max_value =value
            counter_max = counter

    for key in bmi_all.keys():
        c+=1
        #find key of minimum value
        if c == counter_min:
            country_min = key
        #find key of maximum value
        if c== counter_max:
            country_max = key

    #find median value
    year_list.sort()
    l = len(year_list)
    #for even number of values
    if l%2 == 0:
        med1 = year_list[l//2]
        med2 = year_list[l//2-1]
        med_value = (med1+med2)/2
    #for odd number of values
    else:
        med_value = year_list[l//2]

    #print output
    print("In", year, "countries with minimun and maximum BMI values were", country_min, "and", country_max, "respectively.")
    print ("Median BMI value in", year, "was", format(med_value, ".3f"), '\n')


#define function to compute men vs women ststistics of BMI
def men_vs_women():
    #reference dictionaries
    bmi_men_header,bmi_men_data=read_file_dic("bmi_men.csv")
    bmi_women_header,bmi_women_data=read_file_dic("bmi_women.csv")
    counter = 0
    men_list = []
    #create empty lists for 3 countries
    china_list = []
    india_list = []
    us_list = []

    ##find values for men`s dictionary
    for key in bmi_men_data.keys():
        #find country China in dictionaty
        if key=='China':
            china_list = bmi_men_data[key]
            l = len(china_list)
            #get values for lat 5 years
            val1 = china_list[l-1]
            val2 = china_list[l-2]
            val3 = china_list[l-3]
            val4 = china_list[l-4]
            val5 = china_list[l-5]
            china_avg_men = (val1+val2+val3+val4+val5)/ 5
        #find country India in dictionaty
        if key == 'India':
            india_list = bmi_men_data[key]
            l = len(india_list)
            #get values for lat 5 years
            val1 = india_list[l-1]
            val2 = india_list[l-2]
            val3 = india_list[l-3]
            val4 = india_list[l-4]
            val5 = india_list[l-5]
            india_avg_men = (val1+val2+val3+val4+val5)/ 5
        #find country United States in dictionaty
        if key == 'United States':
            us_list = bmi_men_data[key]
            l = len(us_list)
            #get values for lat 5 years
            val1 = us_list[l-1]
            val2 = us_list[l-2]
            val3 = us_list[l-3]
            val4 = us_list[l-4]
            val5 = us_list[l-5]
            us_avg_men = (val1+val2+val3+val4+val5)/ 5

    ##find values for women`s dictionary
    for key in bmi_women_data.keys():
        #find country China in dictionaty
        if key=='China':
            china_list = bmi_women_data[key]
            l = len(china_list)
            #get values for lat 5 years
            val1 = china_list[l-1]
            val2 = china_list[l-2]
            val3 = china_list[l-3]
            val4 = china_list[l-4]
            val5 = china_list[l-5]
            china_avg_women = (val1+val2+val3+val4+val5)/ 5
        #find country India in dictionaty
        if key == 'India':
            india_list = bmi_women_data[key]
            l = len(india_list)
            #get values for lat 5 years
            val1 = india_list[l-1]
            val2 = india_list[l-2]
            val3 = india_list[l-3]
            val4 = india_list[l-4]
            val5 = india_list[l-5]
            india_avg_women = (val1+val2+val3+val4+val5)/ 5
        #find country United States in dictionaty
        if key == 'United States':
            us_list = bmi_women_data[key]
            l = len(us_list)
            #get values for lat 5 years
            val1 = us_list[l-1]
            val2 = us_list[l-2]
            val3 = us_list[l-3]
            val4 = us_list[l-4]
            val5 = us_list[l-5]
            us_avg_women = (val1+val2+val3+val4+val5)/ 5

    #compute percentage difference for China
    if china_avg_men == china_avg_women:
        china_diff = 100
    if china_avg_men != china_avg_women:
        china_diff = (abs(china_avg_men - china_avg_women)/china_avg_women)*100

    #compute percentage difference for India
    if india_avg_men == india_avg_women:
        india_diff = 100
    if india_avg_men != india_avg_women:
        india_diff = (abs(india_avg_men - india_avg_women)/india_avg_women)*100

    #compute percentage difference for US
    if us_avg_men == us_avg_women:
        us_diff = 100
    if us_avg_men != us_avg_women:
        us_diff = (abs(us_avg_men - us_avg_women)/us_avg_women)*100

    #print out results
    print("*** China ***")
    print("Men: ", format(china_avg_men, '.2f'))
    print("Women: ", format(china_avg_women, '.2f'))
    print("Difference in percentage: ", format(china_diff, '.2f'), "%", '\n')

    print("*** India ***")
    print("Men: ", format(india_avg_men, '.2f'))
    print("Women: ", format(india_avg_women, '.2f'))
    print("Difference in percentage: ", format(india_diff, '.2f'), "%", '\n')

    print("*** United States ***")
    print("Men: ", format(us_avg_men, '.2f'))
    print("Women: ", format(us_avg_women, '.2f'))
    print("Difference in percentage: ", format(us_diff, '.2f'), "%", '\n')


#define function to draw life expectancy plot
def life_data(country):
    #reference list
    life_header, life_list = read_file_list("life.csv")
    #get country name from user and set it for lower letters


    for line in life_list:
        name = line[0]
        name.lower()
        #check if user`s input equals to country w/ lower letters within the list
        if country==name.lower():
            #get the list out of line
            country_list = line
            print("Plot for", line[0], "opens in a new window", '\n')


    ##draw life expectancy plot
    #set x,y
    plt.plot(life_header[1::], country_list[1::], 'b*-')
    #name x axes
    plt.xlabel("Years", color = 'red')
    #name y axes
    plt.ylabel("Life expectancy", color = 'red')
    #name the graph
    plt.title("Life expectancy trend", color='blue')

    #display graph
    plt.show()



#define function to draw correlation plot
def correlation():
    #reference values
    bmi_all_header, bmi_all = create_bmi_all()
    life_header, life_list = read_file_list("life.csv")

    ## create a list of average values for life expectancy
    #set lists`s values as float numbers
    lst = [[float(x) for x in line[1::]]for line in life_list]
    #compute total for each year
    totals = [ sum(i) for i in zip(*lst) ]
    #find average for each year
    avg_life = []
    for num in totals:
        avg_life.append(num/len(life_list))

    ## create a list of average values for BMI
    b_list = []
    bmi_list = []
    #compute total for each year
    for line in bmi_all:
        b_list = bmi_all[line]
        bmi_list.append(b_list)
        total = [ sum(j) for j in zip(*bmi_list) ]
    #find average for each year
    avg_bmi = []
    for k in total:
        avg_bmi.append(k/len(bmi_list))


    ##draw correlation plot
    #set axes x, y1, y2
    x_data = life_header[1::]
    y1_data = avg_life
    y2_data = avg_bmi

    #create x and y1
    fig = plt.figure()
    ax1 = fig.add_subplot()
    ax1.set_xlabel('Years')
    ax1.plot(x_data, y1_data,'b*-')
    ax1.tick_params(axis='y', labelcolor='blue')
    ax1.set_ylabel('Life expectancy', color='blue')

    #create a second axes that shares the same x-axis
    ax2 = ax1.twinx()
    ax2.plot(x_data, y2_data, 'ro-')
    ax2.tick_params(axis='y', labelcolor='red')
    ax2.set_ylabel('BMI', color='red')

    #set name for graph
    plt.title("Correlation between BMI and life expectancy", color='green')

    #display the graph
    plt.show()


#call main function
main()
