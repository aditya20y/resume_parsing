# -*- coding: utf-8 -*-
# import docx
import re
import textract
# import nltk
# import numpy
# from numpy.core import multiarray
# import MySQLdb
import datetime
import os

f = open("Test1.html", "a")
edu_line = open("education_paragraph.txt", "a")

summary = ""
total_num_of_resume = ""
pattern_not_found1 = ""
pattern_found = ""

message = "<html>""<table border = '1' width = '600'><tr><th>File Name</th><th>Pattern Found</th></tr>"
detail_message = ''
total_no_of_resume = 0
pattern_not_found = 0

counter = 1



dirs = os.listdir("C:\Python27\Scripts\\tutorial1\\tutorial1\\AI resume for test\\All 50 resume")

for dir in dirs:
    try:
        filepath = "C:\Python27\Scripts\\tutorial1\\tutorial1\\AI resume for test\\All 50 resume" + "\\" + dir
        full_text = textract.process(filepath)
        total_no_of_resume = total_no_of_resume + 1

        # removing spaces.
        full_text_without_space = full_text.strip()
        full_text_lower_case = full_text_without_space.lower()
        # full_text_lower_case1 = unicode(full_text_lower_case, 'utf-8')
        # print (full_text_lower_case)

        # Spliting resume content in to lines.
        resume_lines = full_text_lower_case.split("\n")

        # Removing empty strings from resume to get the accurate index.
        str_list = list(filter(None, resume_lines))

        st = ""
        for i in str_list:
            st = st + i.strip() + "\n".encode('UTF-8')
        # print (st)
        st1 = st.split("\n")
        # for i in st1:
        #     print i
        #     print("\n")


        # Total number of lines.
        len_of_list = len(st1)
        # print (len_of_list)
        ind_list = []

        # connecting to database
        # mydb = MySQLdb.connect(host='localhost',
        #        user='root',
        #        passwd='aditya',
        #        db='student_database')
        #
        # cursor = mydb.cursor()
        # cursor.execute("SELECT * FROM student_data_college")
        # college_rows = cursor.fetchall()
        # cursor.execute("SELECT * FROM student_data_company")
        # company_rows = cursor.fetchall()

        # Empty lists to store the paragraphs.
        education_para = []
        experience_para = []
        project_para = []
        skills_para = []
        education_details = []
        all_detail = []

        # for educational details
        college_name = "NA"
        course = ""
        branch = ""
        year_of_passing = ""
        aggregate = ""

        # for skills
        skills = []

        # for experience details
        designation = ""
        start_date = ""
        end_date = ""
        company_name = "NA"

        # for project details
        project_title = ""
        project_role = ""
        project_client = ""
        project_team_size = ""
        project_description = ""
        project_duration = ""

        # personal details
        first_name = ''
        last_name = ''
        ph = ''
        em = ''
        do = ''


        def is_education(str_list1):
            education_keyword = ["academic credentials", "education", "academics", "academic:", "academic details",
                                 "scholastics", "academic summary", "education details", "educational details:",
                                 "scholastics/ educational qualifications - b.e. aggregate pointer/ percentage: 7.91 cgpa",
                                 "educational qualification:", "highest qualification", "education:",
                                 "accomplishments & educational background", "education:-", "academic profile",
                                 "educational details", "educational qualification", "academic background:",
                                 "education details:", "academic qualifications:", "academic background",
                                 "academic qualification:", "education background", "education qualification:",
                                 "educational qualifications"]
            ind_of_education = 0
            for edu in education_keyword:
                try:
                    ind_of_education = str_list1.index(edu)
                except:
                    pass
            # print ind_of_education
            return ind_of_education, education_keyword


        def is_project(str_list1):
            projects_keyword = ["projects worked on", "project details:", "project details", "project experiences",
                                "project information", "project summary:", "projects summary"
                                "projects", "project#1:", 'project #1', "project name: honeypot",
                                "projects working/completed", "projects handled", "project easeapp.io", "project",
                                "project specifies:", "project profile", "project overview", "project profile:", "project 1:",
                                "project1", "deep learning projects", "projects handled:", "projects:", "projects profile:",
                                "key projects:", "project #1:", "project1:", "projects",]
            ind_of_project = 0
            for pro in projects_keyword:
                try:
                    ind_of_project = str_list1.index(pro)
                except:
                    pass
            # print ind_of_project
            return ind_of_project, projects_keyword


        def is_experience(str_list1):
            experience_keyword = ["summary of work experience", "internship", "professional experience:",
                                  "professional experience", "professional summary", "professional summary:", "experience",
                                  "work experience", "professional synopsis", "work experience:", "employment history",
                                  "experiences", "professional experience:-", "career profile", "experience summary:",
                                  "experience summary", "organizational experience", "experience:", "organisational experience",
                                  ]
            ind_of_experience = 0
            for exp in experience_keyword:
                try:
                    ind_of_experience = str_list1.index(exp)
                except:
                    pass
            # print ind_of_experience
            return ind_of_experience, experience_keyword


        def is_skills(str_list1):
            skills = ["technical skills:", "skills & abilities", "technical proficiency", "technical proficiency:",
                      " web technologies:", "skill set",
                      "technical expertise", "technical skills", "technical skill set:",
                      "core competencies/ technical skill sets", "it expertise", "proficiency forte:",
                      "skills and certifications:", "key skills", "it skills", "tools & technologies", "summary of skills",
                      "technology", "it exposure", "technical skills:-", "skills", "technical summary", "technical environment:",
                      "technical expertise:", "technologies:", "software skill set", "it skill set:"]
            ind_of_skill = 0
            for sk in skills:
                try:
                    ind_of_skill = str_list1.index(sk)
                except:
                    pass
            # print ind_of_skill
            return ind_of_skill, skills


        def para_extract():
            education_index, education_keyword = is_education(st1)
            project_index, projects_keyword = is_project(st1)
            experience_index, experience_keyword = is_experience(st1)
            skill_index, skills = is_skills(st1)

            ind_list.append(education_index)
            ind_list.append(project_index)
            ind_list.append(experience_index)
            ind_list.append(skill_index)
            ind_list.sort()
            # print ind_list

            for i in ind_list:
                # print(st1[i])
                for edu in education_keyword:
                    if st1[i] == edu:
                        ed_ind = ind_list.index(i)
                        try:
                            for e in range(ind_list[ed_ind], ind_list[ed_ind + 1]):
                                education_para.append(st1[e])
                                # print (str_list[e])
                        except:
                            for e in range(ind_list[ed_ind], len_of_list):
                                education_para.append(st1[e])
                                # print (str_list[e])
                    else:
                        pass

                for pro in projects_keyword:
                    if st1[i] == pro:
                        ed_ind = ind_list.index(i)
                        try:
                            for e in range(ind_list[ed_ind], ind_list[ed_ind + 1]):
                                project_para.append(st1[e])
                                # print (str_list[e])
                        except:
                            for e in range(ind_list[ed_ind], len_of_list):
                                project_para.append(st1[e])
                                # print (str_list[e])

                    else:
                        pass

                for exp in experience_keyword:
                    if st1[i] == exp:
                        ed_ind = ind_list.index(i)
                        try:
                            for e in range(ind_list[ed_ind], ind_list[ed_ind + 1]):
                                experience_para.append(st1[e])
                                # print (str_list[e])
                        except:
                            for e in range(ind_list[ed_ind], len_of_list):
                                experience_para.append(st1[e])
                                # print (str_list[e])

                    else:
                        pass

                for sk in skills:
                    if st1[i] == sk:
                        ed_ind = ind_list.index(i)
                        try:
                            for e in range(ind_list[ed_ind], ind_list[ed_ind + 1]):
                                skills_para.append(st1[e])
                                # print (str_list[e])
                        except:
                            for e in range(ind_list[ed_ind], len_of_list):
                                skills_para.append(st1[e])
                                # print (str_list[e])

                    else:
                        pass

            # print("**************************************************************************")
            # print("**************************************************************************")
            # print(education_para)
            # print("**************************************************************************")
            # print("**************************************************************************")
            # print (project_para)
            # print("**************************************************************************")
            # print("**************************************************************************")
            # print (experience_para)
            # print("**************************************************************************")
            # print("**************************************************************************")
            # print (skills_para)

        # print (education_para)


        def get_personal_detail(full_text):
            p0 = full_text[0]
            p1 = full_text[1]

            if p0 != "Resume" and p0 != "RESUME" and p0 != "CV" and p0 != "CurriculumVitae" and p0 != "":
                name = re.findall("[A-Z][a-z]*", p0, re.I)
                name1 = " ".join(name)
                # print (name1)
                try:
                    n = name1.split()
                    first_name = n[0]
                    last_name = n[1]
                    # print ("first name is ", first_name)
                    # print ("Last name is ", last_name)
                except:
                    first_name = n[0]
                    last_name = ""
                    # print ("first name is ", first_name)
            elif p1 != "Resume" and p1 != "RESUME" and p1 != "CV" and p1 != "CurriculumVitae" and p1 != "":
                name = re.findall("[A-Z][a-z]*", p1, re.I)
                name1 = " ".join(name)
                try:
                    n = name1.split()
                    first_name = n[0]
                    last_name = n[1]
                    # print ("first name is ", first_name)
                    # print ("Last name is ", last_name)
                except:
                    first_name = n[0]
                    last_name = ""
                    # print ("first name is ", first_name)
            else:
                first_name = "NA"
                last_name = "NA"

            ph = ''
            em = ''
            do1 = ''
            for line in full_text:
                # print line
                # line = para.text.encode('UTF-8')
                phone = re.search("\d{2}\-\d{10}|\d{10}", line)
                if phone:
                    ph = phone.group(0)
                    # print ("Phone", ph)
                else:
                    ph = "NA"

                email = re.search("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}", line)
                if email:
                    em = email.group(0)
                    # print ("Email", em)
                    break
                else:
                    em = "NA"

                date_of_birth = ["date of birth", "dob"]
                for line1 in full_text:
                    for i in date_of_birth:
                        dob1 = re.findall(i, line1, re.I)

                        if dob1:
                            dob1 = " ".join(dob1).replace(" ", "")
                            line1 = line1.replace("\t", "")
                            line1 = line1.replace(" ", "")
                            try:
                                do = line1.split(":")
                                do1 = do[1]
                                print("DOB", do1)
                            except:
                                try:
                                    do = line1.split("-")
                                    do1 = do[1]
                                    print("DOB", do1)
                                except:
                                    pass

                            break
                        else:
                            do1 = "NA"
                    if do1 != "NA":
                        break
            return first_name, last_name, ph, em, do1


        def get_education_details(edu_para):

            # def get_college_name():
            #     college_name = ""
            #     for row in college_rows:
            #         c = re.findall(row[1], " ".join(edu_para), re.I)
            #         if c:
            #             college_name = c
            #             break
            #         else:
            #             college_name = "NA"
            #
            #     # print('College', college_name)
            #     return college_name



                # def college_name_other():
                #     pass
                #     # tokenized_doc = nltk.word_tokenize(" ".join(edu_para))
                #     # tagged_sentences = nltk.pos_tag(tokenized_doc)
                #     # print (tagged_sentences)
                #     # # print ("------------------------------------------------")
                #     # grammar = r'CompanyName: {<NN.*><NN.*>}'
                #     # chunk_parser = nltk.RegexpParser(grammar)
                #     # chunked = chunk_parser.parse(tagged_sentences)
                #     # for subtree in chunked.subtrees(filter=lambda t: t.label() == 'CompanyName'):
                #     #     college = ' '.join([w for w, t in subtree.leaves()])
                #     # # print ("*********************************************************************")
                #     # print ("College Name:", college)

            def get_branch_name():
                branch_keyword = ["information technology", "mechanical", 'electrical', "Comp Science",
                                  "computer science", "Electronics", "Electronics & Instrumentation", "CSE", "Data Analytics", "E&C"]
                for i in edu_para:
                    for br in branch_keyword:
                        branch_name = re.search(br, i, re.I)
                        if branch_name:
                            branch = branch_name.group()
                            # print("branch", branch)
                            break
                        else:
                            branch = "NA"
                    if branch != "NA":
                        break
                return branch


            def get_course_name():
                course_keyword = ["mba", "m.tech", "mtech", "mca", "b-tech", "b.tech", "Btech", "bca", "bsc", "Bachelors of Engineering",
                                  "master of computer applications", "bachelor of computer applications", "B.E (Electronics)",
                                  "Masters In Computer Applications ", "Post Graduate", "Bachelor of Technology ",
                                  "Master Of Business Administration ", "master of computer application",
                                  "bachelor of computer application", "Bachelor of Information Technology"]
                for i in edu_para:
                    for cr in course_keyword:
                        course_name = re.search(cr, i, re.I)
                        if course_name:
                            course = course_name.group()
                            # print("course", course)
                            break
                        else:
                            course = "NA"

                    if course != "NA":
                        break

                return course
            # print("course_ashok", get_course_name())

            def get_year_of_passing():
                for i in edu_para:
                    year = re.findall("(\d{4}-\d{4}|\d{4})", i)
                    if year:
                        year_of_passing = year
                        # print ("Year", year_of_passing)
                        break
                    else:
                        year_of_passing = "NA"

                return year_of_passing
            # print ("year_adi",get_year_of_passing())
                # def pattern1():
                #     year = re.findall("(\d{4}-\d{4})", "".join(edu_para))
                #     # return year
                #     if year:
                #         year_of_passing = year
                #         print("year", year_of_passing)
                #     return year_of_passing
                #
                # def pattern2():
                #     year = re.findall("(\d{4})", "".join(edu_para))
                #     # return year
                #     if year:
                #         year_of_passing = year
                #         print("year", year_of_passing)
                #     return year_of_passing

            def get_marks():
                for i in edu_para:
                    marks = re.findall("(\d{2}[.]\d{2}[%]|\d{2}[.]\d{2}|\d{2}[%]|\d{2}[.]\d{1}[%]|\d{1}[%])", i)
                    if marks:
                        aggregate = marks
                        # print ("Marks", aggregate)
                        break
                    else:
                        aggregate = "NA"
                return aggregate
            # print ("marks_adi", get_marks())
            # print ("course_adi", get_course_name())
            return get_branch_name(), get_course_name(), get_year_of_passing(), get_marks()



        def get_skills(sk_para):
            skills_keyword = ["python", "html", "Java Script", "django", "css", "bootstarp", "SQL", "Unix", "Windows", "Oracle",
                              "SharePoint", "MVC", "Design Patterns", "MEF", "Prism", "Entity", "Framework", "Ajax", "Jquery",
                              "C#", "VB.net", "SQL server", "Networking", "CCNA", "CCNP", "Network Design",
                              "Cisco Certified Network Associate ", "C", "Firmware Development", "Linux Device driver",
                              "NVMe protocol", "Linux Internals","Tensor Flow", "Linear regression",
                              "Logistic Regression", "Decision Tree", "Random Forest", "KNN", "Naive Bayes", "Clustering",
                              "AI", "Deep learning", "Machine Learning", "Neural Network", "Deep Learning",
                              "Tensorflow", "Pandas", "Numpy", "Matplotlib", "RHEL", "SAN", "DAN", "OpenCV", "Nintex",
                              "Jenkins", "iSCSI", "HDFS", "Spark", "HIVE", "JSP", "PHP", "Natural Language processing",
                              "NLTK", "Java", "Perl", "PL/SQL"]
            for i in sk_para:
                for s in skills_keyword:
                    sk = re.findall(s, i, re.I)
                    if sk:
                        for dup in sk:
                            if dup not in skills:
                                skills.append(dup)
            # print ("skills", skills)
            return skills




        def get_experience_detail(exp_para):
            # def get_company_name():
            #
            #     company_name = ""
            #     for row in company_rows:
            #         # print row[1]
            #         c = re.findall(row[1], " ".join(exp_para), re.I)
            #         if c:
            #             company_name = c
            #             break
            #         else:
            #             company_name = "NA"
            #     # print('Company', company_name)
            #     return company_name





            def get_designation():
                desig_keyword = ["Senior Software Engineer", "Senior Systems Engineer", "SAP ABAP Consultant ",
                                 "Machine Learning Engineer ", "Associate Business Analyst", "Data Scientist ",
                                 "Data Analyst/Scientist", "Software Developer", "Storage Tester", "Specialist",
                                 "Team Lead", "Software Engineer", "Data Specialist", "Software engineer",
                                 "Senior System Engineer", "ML Engineer", "Data Engineer", "Mainframe Developer",
                                 "Module Lead", "Senior Implementation Data Engineer", "Implementation Engineer",
                                 "Win automation developer", "Storage Test Engineer", "Associate Software Engineer",
                                 "Test Consultant", "Tester", "SDET ", "Test Engineer", "Automation Test Engineer",
                                 "Storage Testing Engineer", "Trainee", "Senior Analyst", "Business Analyst",
                                 "Python Developer "]
                for i in exp_para:
                    for desig in desig_keyword:
                        desig1 = re.search(desig, i, re.I)
                        if desig1:
                            designation = desig1.group()
                            # print ("Designation", designation)
                            break
                        else:
                            designation = "NA"
                    if designation != "NA":
                        break
                return designation

            def get_duration():
                def pattern1():
                    for i in exp_para:
                        x = re.findall("\d{4}", i)
                        if x:

                            try:
                                # pattern April, 2014 - July, 2017
                                x1 = i.split(" ")
                                ind1 = x1.index("-")
                                # print(x)
                                # print (ind1)
                                # print (x1)
                                start_date = x1[ind1 - 2] + x1[ind1 - 1]
                                end_date = x1[ind1 + 1] + x1[ind1 + 2]
                                # print("Start Date", start_date)
                                # print ("End Date", end_date)
                            except:
                                try:
                                    # pattern July, 2017 - Present
                                    start_date = x1[ind1 - 2] + x1[ind1 - 1]
                                    end_date = x1[ind1 + 1]
                                    # print("Start date", start_date)
                                    # print ("End Date", end_date)
                                except:
                                    start_date = "NA"
                                    end_date = "NA"
                        else:
                            start_date = "NA"
                            end_date = "NA"

                def pattern2():
                    for i in exp_para:
                        x = re.findall("\d{4}", i)
                        if x:

                            try:
                                # pattern July 2017 to july 2018
                                x1 = i.split(" ")
                                ind1 = x1.index("to")
                                # print(x)
                                # print (ind1)
                                # print (x1)
                                start_date = x1[ind1 - 2] + x1[ind1 - 1]
                                end_date = x1[ind1 + 1] + x1[ind1 + 2]
                                # print("Start Date", start_date)
                                # print ("End Date", end_date)
                            except:
                                try:
                                    # pattern July, 2017 to Present
                                    start_date = x1[ind1 - 2] + x1[ind1 - 1]
                                    end_date = x1[ind1 + 1]
                                    # print("Start Date", start_date)
                                    # print ("End Date", end_date)
                                except:
                                    start_date = "NA"
                                    end_date = "NA"
                        else:
                            start_date = "NA"
                            end_date = "NA"
                    return start_date, end_date

                return pattern1(), pattern2()
            return get_designation(), get_duration()




        def get_project_detail(pro_para):

            def get_project_role():
                role_keyword = ["role", "Roles and Responsibilities", "responsibilities", "designation"]


                for i in pro_para:
                    for r in role_keyword:
                        role = re.findall(r, i, re.I)
                        if role:
                            role = " ".join(role).replace(" ", "")
                            line = i.replace("\t", "")
                            line1 = line.replace(" ", "")
                            # print line1
                            try:

                                split_in_words = line1.split(":")
                                # print split_in_words
                                role_ind = split_in_words.index(role) # checking the index of keyword to solve duplicate
                                # print("role ind", role_ind)
                                if role_ind < 1:
                                    project_role = split_in_words[1]
                                    # print("Project Role", project_role)
                            except:
                                try:
                                    split_in_words = line1.split("-")
                                    role_ind = split_in_words.index(role)
                                    if role_ind < 1:
                                        project_role = split_in_words[1]
                                        # print("Project Role", project_role)
                                except:
                                    try:
                                        if role_ind < 1:
                                            role_ind = pro_para.index(i)
                                            project_role = pro_para[role_ind + 1]
                                            # print("Project Role", project_role)
                                            # print("\n")
                                            # desc1.append(project_description)
                                            role_ind = pro_para.pop(role_ind)

                                    except:
                                        project_role = "NA"
                                        # print ("Project Role", project_role)
                        else:
                            project_role = "NA"

                return project_role


            def get_project_title():
                title_keyword = ["project title", "project name", "title", "product name", "project", "Product"]


                for i in pro_para:
                    for t in title_keyword:
                        title = re.findall(t, i, re.I)
                        if title:
                            # print ("title line", i)
                            title = " ".join(title).replace(" ", "")
                            line = i.replace("\t", "")
                            line1 = line.replace(" ", "")
                            # print ("adsi", line1)
                            try:
                                # print i
                                split_in_words = line1.split(":")
                                # print (split_in_words)
                                title_ind = split_in_words.index(title)  # checking the index of keyword to solve duplicate
                                # print ("title ind", title_ind)
                                if title_ind < 1:
                                    project_title = split_in_words[1]

                                    # print ("Project Title", project_title)
                            except:
                                try:
                                    split_in_words = line1.split("-")
                                    title_ind = split_in_words.index(title)
                                    # print (title_ind)
                                    if title_ind < 1:
                                        project_title = split_in_words[1]

                                        # print ("Project Title", project_title)
                                except:
                                    try:
                                        if title_ind < 1:
                                            title_ind = pro_para.index(i)
                                            # print title_ind
                                            project_title = pro_para[title_ind + 1]
                                            # print("Project Title", project_title)
                                            # print("\n")
                                            # desc1.append(project_description)
                                            title_ind = pro_para.pop(title_ind)

                                    except:
                                        project_title = "NA"
                                       # print ("Project Title", project_title)
                                    break

                        else:
                            project_title = "NA"

                    if project_title != "NA":
                        break

                return project_title


            def get_project_client():
                client_keyword = ["Client", "Client name", "employer", "employer name", "company name", "Client:",
                                  "Project Client", "Organization"]


                for i in pro_para:
                    for c in client_keyword:
                        client = re.findall(c, i, re.I)
                        if client:
                            client = " ".join(client).replace(" ", "")
                            line = i.replace("\t", "")
                            line1 = line.replace(" ", "")
                            try:
                                split_in_words = line1.split(":")
                                # print ("split", split_in_words)
                                # print (client[0])
                                client_ind = split_in_words.index(client)
                                # print ("client index", client_ind)
                                if client_ind < 1:
                                    project_client = split_in_words[1]
                                    # print ("Project Client", project_client)

                            except:
                                try:

                                    split_in_words = i.split("-")
                                    client_ind = split_in_words.index(client)
                                    # print ("client index",client_ind)
                                    if client_ind < 1:
                                        project_client = split_in_words[1]
                                        # print ("Project Client", project_client)
                                except:

                                    try:
                                        if client_ind < 1:
                                            client_ind = pro_para.index(i)
                                            # print ("client index", client_ind)
                                            project_client = pro_para[client_ind + 1]
                                            # print("Project Client", project_client)
                                            # print("\n")
                                            # desc1.append(project_description)
                                            client_ind = pro_para.pop(client_ind)
                                    except:
                                        project_client = "NA"
                                        # print ("Project Client", project_client)
                                    break
                        else:
                            project_client = "NA"
                    if project_client != "NA":
                        break

                return project_client



            def get_project_team():
                team_keyword = ["Team Size", "size :", "team members"]
                project_team_size = ""

                for i in pro_para:
                    for te in team_keyword:
                        team_size = re.findall(te, i, re.I)

                        if team_size:
                            team_size = " ".join(team_size).replace(" ", "")
                            # print team_size
                            line = i.replace("\t", "")
                            line1 = line.replace(" ", "")
                            # print line1
                            try:
                                split_in_words = line1.split(":")
                                team_ind = split_in_words.index(team_size)
                                # print ("team ind", team_ind)
                                if team_ind < 1:
                                    project_team_size = split_in_words[1]
                                    # print ("Project Team Size", project_team_size)
                            except:
                                try:
                                    split_in_words = i.split("-")
                                    team_ind = split_in_words.index(team_size)
                                    # print (team_ind)
                                    if team_ind < 1:
                                        project_team_size = split_in_words[1]
                                        # print ("Project Team Size", project_team_size)
                                except:
                                    try:
                                        if team_ind < 1:
                                            team_ind = pro_para.index(i)
                                            project_team_size = pro_para[team_ind + 1]
                                            # print("Project Team Size", project_team_size)
                                            # print("\n")
                                            # desc1.append(project_description)
                                            team_ind = pro_para.pop(team_ind)
                                    except:
                                        project_team_size = "NA"
                                        # print ("Team Size", project_team_size)
                                    break
                        else:
                            project_team_size = "NA"
                    if project_team_size != "NA":
                        break

                return project_team_size


            def get_project_description():
                description_keyword = ["Description", "about project", "Project Descriptions ", "Project Description:",
                                       "Description:", "Project Overview"]
                desc1 = []
                # print pro_para
                project_description = ""


                for i in pro_para:
                    # print i
                    for d in description_keyword:
                        description = re.findall(d, i, re.I)
                        # print ("description", description)
                        if description:
                            description = " ".join(description).replace(" ", "")
                            # print ("description", description)
                            line = i.replace("\t", "")
                            line1 = line.replace(" ", "")
                            # print line1
                            try:
                                split_in_words = line1.split(":")
                                desc_ind = split_in_words.index(description)  # checking the index of keyword to solve duplicate
                                # print("desc ind", desc_ind)
                                if desc_ind < 1:
                                    # print i
                                    project_description = split_in_words[1]
                                    # print("Project Description", project_description)
                                    # print("\n")
                            except:
                                try:
                                    split_in_words = line1.split("-")
                                    desc_ind = split_in_words.index(description)  # checking the index of keyword to solve duplicate
                                    # print("desc ind", desc_ind)
                                    if desc_ind < 1:
                                        project_description = split_in_words[1]
                                        # print("Project Description", project_description)
                                except:
                                    try:
                                        if desc_ind < 1:
                                            desc_ind = pro_para.index(i)
                                            # print("desc ind", desc_ind)
                                            project_description = pro_para[desc_ind + 1]
                                            # desc1.append(desc)
                                            # print ("Project Description", project_description)
                                            # print("\n")
                                            desc1.append(project_description)
                                            desc_ind = pro_para.pop(desc_ind)
                                    except:
                                        project_description = "NA"
                                        # print ("Project Description", project_description)
                                    break
                        else:
                            project_description = "NA"
                    if project_description != "NA":
                        break

                return project_description


            def get_project_duration():
                duration_keyword = ["Period", "duration", ]
                desc1 = []
                # print pro_para


                for i in pro_para:
                    for du in duration_keyword:
                        duration = re.findall(du, i, re.I)
                        if duration:
                            line = i.replace("\t", "")
                            line1 = line.replace(" ", "")
                            try:
                                project_duration = line1.split(":")[1]
                                # print("Project Duration", project_duration)
                                # print("\n")
                            except:
                                try:
                                    project_duration = line1.split("-")[1]
                                    # print("Project Duration", project_duration)
                                    # print("\n")
                                except:
                                    try:
                                        duration_ind = pro_para.index(i)
                                        project_duration = pro_para[duration_ind + 1]
                                        # desc1.append(desc)
                                        # print ("Project Duration", project_duration)
                                        # print("\n")

                                    except:
                                        project_duration = "NA"
                                        # print ("Project duration", project_duration)
                                    break
                        else:
                            project_duration = "NA"
                    if project_duration != "NA":
                        break
                return project_duration
            return get_project_role(), get_project_title(), get_project_client(), get_project_team(), get_project_description(), get_project_duration()






        para_extract()

        # print(education_para)
        # edu_line.write(" ".join(education_para))
        # edu_line.write("\n")
        # edu_line.write("********************************************************************************************************************************************************************************")
        # edu_line.write("***********************************************************************************************************************************************************************")
        # edu_line.write("\n")

        # print("Education", education_para)
        # print("\n")
        # # print (" ".join(education_para))
        # print("\n")
        # print ("Skills", skills_para)
        # print("\n")
        # print ("Experience", experience_para)
        # print("\n")
        # print ("Project", project_para)
        # print("\n")

        # # print("\n")
        # get_skills(skills_para)
        # # print("\n")
        # get_experience_detail(experience_para)
        # get_personal_detail(resume_lines)
        # print("\n")
        # get_project_detail(project_para)
        # print("\n")
        # personal_detail = get_personal_detail(resume_lines)
        # education_detail = get_education_details(education_para)
        # skills_detail = get_skills(skills_para)
        # job_detail = get_experience_detail(experience_para)
        # projects_detail = get_project_detail(project_para)


        # print("personal detail", personal_detail)
        # print("\n")
        # print("Education details", education_detail)
        # print("\n")
        # print ("skills details", skills_detail)
        # print("\n")
        # print("Job Details", job_detail)
        # print("\n")
        # print ("projects detail", projects_detail)


        first_name, last_name, phone, email, dob = get_personal_detail(resume_lines)

        # print("First name", first_name)
        # print("\n")
        # print("Last name", last_name)
        # print("\n")
        # print("Phone", phone)
        # print("\n")
        # print("email", email)
        # print("\n")
        # print("DOB", dob)
        # print("\n")

        # print ("************************************************************************")
        # education_detail = get_education_details(education_para)
        branch, course, year_of_passing, aggregate = get_education_details(education_para)
        # print("college name", college_name)
        # print("\n")
        # print("Branch name", branch)
        # print("\n")
        # print("Course Name", course)
        # print("\n")
        # print("Passing year", year_of_passing)
        # print("\n")
        # print("Marks", aggregate)
        # print("\n")
        # print ("************************************************************************")

        skills_detail = get_skills(skills_para)
        # print ("Skills", skills_detail)
        # print("\n")
        # print ("************************************************************************")

        # job_detail = get_experience_detail(experience_para)
        designation, exp_date = get_experience_detail(experience_para)

        # print("company name", company_name)
        # print("\n")
        # print("designation", designation)
        # print("\n")
        # print("Start Date", date)
        # print("\n")
        # # print("End date", end_date)
        # # print("\n")
        # print ("************************************************************************")

        # projects_detail = get_project_detail(project_para)
        project_role, project_title, project_client, project_team_size, project_description, project_duration = get_project_detail(project_para)

        # print("Role", project_role)
        # print("\n")
        # print("Title", project_title)
        # print("\n")
        # print("Client", project_client)
        # print("\n")
        # print("Team Size", project_team_size)
        # print("\n")
        # print("Description", project_description)
        # print("\n")
        # print("Duration", project_duration)
        # print("\n")
        # print ("************************************************************************")

        all_detail.append(first_name)
        all_detail.append(last_name)
        all_detail.append(phone)
        all_detail.append(email)
        all_detail.append(dob)
        all_detail.append(college_name)
        all_detail.append(branch)
        all_detail.append(course)
        all_detail.append(year_of_passing)
        all_detail.append(aggregate)
        all_detail.append(skills_detail)
        all_detail.append(company_name)
        all_detail.append(designation)
        all_detail.append(exp_date)
        all_detail.append(project_role)
        all_detail.append(project_title)
        all_detail.append(project_client)
        all_detail.append(project_team_size)
        all_detail.append(project_description)
        all_detail.append(project_duration)


        # print (all_detail)

        # f = open("Test.html", "a")
        # message = "<html>""<table border = '1' width = '200'><tr><th>File Name</th><th>Pattern Found</th></tr>"

        for i in all_detail:
            # print i
            if i == "NA":
                message += '<tr bgcolor="#FA8072"><td width = "400"><a href= "#' + str(counter) + '">' + " ".join(dir) +'<td align="center" width = "100">No</td>''</a></td></tr>'
                pattern_not_found = pattern_not_found + 1
                break

        else:
            message += '<tr bgcolor="#FA8072"><td width = "400"><a href= "#' + str(counter) + '">' + " ".join(dir) +'<td align="center  width = "100">Yes</td>''</a></td></tr>'

        detail_message += '<div id = "' + str(counter) + '">'
        detail_message += "<table border = '1' width = '600'><tr><th>File Name</th><th>Result</th></tr>"

        detail_message += '<tr><td width = "400">' + " ".join(dir) + '<td align="center" width = "600">Fail</td>''</td></tr>'
        if first_name == "NA":
            detail_message += '<tr bgcolor="#FA8072"><td width = "400">First Name</td><td width = "600">' + " ".join(first_name) + '</td></tr>'
        else:
            detail_message += '<tr><td width = "400">First Name</td><td width = "600">' + " ".join(
                first_name) + '</td></tr>'
        if last_name == "NA":
            detail_message += '<tr bgcolor="#FA8072"><td width = "400">Last Name</td><td width = "600">' + " ".join(last_name) + '</td></tr>'
        else:
            detail_message += '<tr><td width = "400">Last Name</td><td width = "600">' + " ".join(last_name) + '</td></tr>'
        if phone == "NA":
            detail_message += '<tr bgcolor="#FA8072"><td width = "400">Phone</td><td width = "600">' + " ".join(phone) + '</td></tr>'
        else:
            detail_message += '<tr><td width = "400">Phone</td><td width = "600">' + " ".join(phone) + '</td></tr>'
        if email == "NA":
            detail_message += '<tr bgcolor="#FA8072"><td width = "400">Email</td><td width = "600">' + " ".join(email) + '</td></tr>'
        else:
            detail_message += '<tr><td width = "400">Email</td><td width = "600">' + " ".join(email) + '</td></tr>'
        if dob == "NA":
            detail_message += '<tr bgcolor="#FA8072"><td width = "400">Date of Birth</td><td width = "600">' + " ".join(dob) + '</td></tr>'
        else:
            detail_message += '<tr><td width = "400">Date of Birth</td><td width = "600">' + " ".join(
                dob) + '</td></tr>'
        if college_name == "NA":
            detail_message += '<tr bgcolor="#FA8072"><td width = "400">College Name</td><td width = "600">' + " ".join(college_name) + '</td></tr>'
        else:
            detail_message += '<tr><td width = "400">College Name</td><td width = "600">' + " ".join(
                college_name) + '</td></tr>'
        if branch == "NA":
            detail_message += '<tr bgcolor="#FA8072"><td width = "400">Branch</td><td width = "600">' + " ".join(branch) + '</td></tr>'
        else:
            detail_message += '<tr><td width = "400">Branch</td><td width = "600">' + " ".join(branch) + '</td></tr>'
        if course == "NA":
            detail_message += '<tr bgcolor="#FA8072"><td width = "400">Course</td><td width = "600">' + " ".join(course) + '</td></tr>'
        else:
            detail_message += '<tr><td width = "400">Course</td><td width = "600">' + " ".join(course) + '</td></tr>'
        if year_of_passing == "NA":
            detail_message += '<tr bgcolor="#FA8072"><td width = "400">Year of Passing</td><td width = "600">' + " ".join(year_of_passing) + '</td></tr>'
        else:
            detail_message += '<tr><td width = "400">Year of Passing</td><td width = "600">' + " ".join(
                year_of_passing) + '</td></tr>'
        if aggregate == "NA":
            detail_message += '<tr bgcolor="#FA8072"><td width = "400">Marks</td><td width = "600">' + " ".join(aggregate) + '</td></tr>'
        else:
            detail_message += '<tr><td width = "400">Marks</td><td width = "600">' + " ".join(aggregate) + '</td></tr>'
        if skills_detail == "NA":
            detail_message += '<tr bgcolor="#FA8072"><td width = "400">Skills</td><td width = "600">' + " ".join(skills_detail) + '</td></tr>'
        else:
            detail_message += '<tr><td width = "400">Skills</td><td width = "600">' + " ".join(
                skills_detail) + '</td></tr>'
        if company_name == "NA":
            detail_message += '<tr bgcolor="#FA8072"><td width = "400">Company Name</td><td width = "600">' + " ".join(company_name) + '</td></tr>'
        else:
            detail_message += '<tr><td width = "400">Company Name</td><td width = "600">' + " ".join(
                company_name) + '</td></tr>'
        if designation == "NA":
            detail_message += '<tr bgcolor="#FA8072"><td width = "400">Designation</td><td width = "600">' + " ".join(designation) + '</td></tr>'
        else:
            detail_message += '<tr><td width = "400">Designation</td><td width = "600">' + " ".join(
                designation) + '</td></tr>'
        # detail_message += '<tr><td>Duration</td><td>' + " ".join(exp_date) + '</td></tr>'
        if project_role == "NA":
            detail_message += '<tr bgcolor="#FA8072"><td width = "400">Project Role</td><td width = "600">' + " ".join(project_role) + '</td></tr>'
        else:
            detail_message += '<tr><td width = "400">Project Role</td><td width = "600">' + " ".join(
                project_role) + '</td></tr>'
        if project_title == "NA":
            detail_message += '<tr bgcolor="#FA8072"><td width = "400">Project Title</td><td width = "600">' + " ".join(project_title) + '</td></tr>'
        else:
            detail_message += '<tr><td width = "400">Title</td><td width = "600">' + " ".join(
                project_title) + '</td></tr>'
        if project_client == "NA":
            detail_message += '<tr bgcolor="#FA8072"><td width = "400">Client</td><td width = "600">' + " ".join(project_client) + '</td></tr>'
        else:
            detail_message += '<tr><td width = "400">Client</td><td width = "600">' + " ".join(
                project_client) + '</td></tr>'
        if project_team_size == "NA":
            detail_message += '<tr bgcolor="#FA8072"><td width = "400">Project Team Size</td><td width = "600">' + " ".join(project_team_size) + '</td></tr>'
        else:
            detail_message += '<tr><td width = "400">Project Team Size</td><td width = "600">' + " ".join(
                project_team_size) + '</td></tr>'
        if project_description == "NA":
            detail_message += '<tr bgcolor="#FA8072"><td width = "400">Project description</td><td width = "600">' + " ".join(project_description) + '</td></tr>'
        else:
            detail_message += '<tr><td width = "400">Project description</td><td width = "600">' + " ".join(
                project_description) + '</td></tr>'
        if project_duration == "NA":
            detail_message += '<tr bgcolor="#FA8072"><td width = "400">Project Duration</td><td width = "600">' + " ".join(project_duration) + '</td></tr>'
        else:
            detail_message += '<tr><td width = "400">Project Duration</td><td width = "600">' + " ".join(
                project_duration) + '</td></tr>'


        detail_message += '<br>'
        detail_message += '<br>'
        detail_message += '<br>'
        detail_message += '<br>'
        detail_message += '<br>'
        detail_message += '<br>'
        detail_message += '<br>'
        detail_message += '<br>'
        detail_message += '<h2 "style = text-align: center;"><a href = "#">HOME</a></h2>'
        detail_message += '</table>'
        detail_message += '</div>'

        counter = counter + 1












    except:
        pass

message += "</table></html>"
summary = "<h2>Summary</h2>"
total_num_of_resume = '<h3>'+'Total No. Of Resume - ' + str(total_no_of_resume) + '</h3>'
pattern_found = '<h3>'+'Pattern Found - ' + str(total_no_of_resume - pattern_not_found) + '</h3>'
pattern_not_found1 = '<h3>'+'Pattern Not Found - ' + str(pattern_not_found) + '</h3>'

f.write(summary)
f.write(total_num_of_resume)
f.write(pattern_found)
f.write(pattern_not_found1)
f.write(message)
f.write(detail_message)
f.close()
edu_line.close()
print("**********")
print("Completed")
print("**********")
# print("Total resume", total_no_of_resume)
# print("PAttern not found", pattern_not_found)
