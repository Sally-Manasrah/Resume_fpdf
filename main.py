from fpdf import FPDF
import pandas as pd

# This project done by Sally Manasrah & Israa Hasanat 
# Read persons information
data = pd.read_csv("data.csv")


# insert data in pdf
def top_right_side(p_index, pdf):
    """
    Given person info,add name and summary to CV.
    """
    pdf.set_font("Arial", size=20)
    pdf.set_xy(55, 10)
    pdf.set_text_color(118, 0, 0)
    pdf.cell(20, 5, txt=data['name'][p_index], ln=2)
    pdf.set_font("Arial", 'B', size=10)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(55, 40)
    pdf.cell(20, 10, txt="Summary", ln=2)
    pdf.set_font("Arial", size=10)
    current_y = pdf.get_y()
    current_x = pdf.get_x()
    pdf.multi_cell(130, 5, data['summary'][p_index])
    pdf.set_xy(current_x, current_y + 43)


def right_side(p_index, pdf):
    """
    Given person info,add experience,education and certifications parts of the CV.
    """
    top_right_side(p_index, pdf)
    headers = ["Experience", "Education", "Certifications"]
    details = [['exp1', 'exp2', 'exp3'], ['edu1', 'edu2'], ['cert1', 'cert2', 'cert3']]
    k = 0
    for header in headers:
        pdf.set_font("Arial", 'B', size=11)
        pdf.cell(20, 10, txt=header, ln=2)
        pdf.set_font("Arial", size=10)
        for detail in details[k]:
            info_list = [s.strip() for s in data[detail][p_index].split(',')]
            current_y = pdf.get_y()
            current_x = pdf.get_x()
            pdf.set_xy(current_x, current_y + 3)
            for info in info_list:
                pdf.cell(30, 5, info, ln=2)
        pdf.set_xy(pdf.get_x(), pdf.get_y() + 5)
        k += 1


def top_left_side(p_index, pdf):
    """
    Given person info,add image and communication details on CV.
    """
    pdf.set_xy(10, 10)
    pdf.image(data['image'][p_index], w=25, h=25)
    pdf.set_font("Arial", size=10)
    pdf.set_text_color(0, 0, 0)
    pdf.set_x(10)
    pdf.cell(20, 10, data['phone'][p_index], ln=2)
    pdf.cell(20, 5, data['email'][p_index], ln=2)
    pdf.cell(20, 5, data['address'][p_index], ln=2)


def left_side(p_index, pdf):
    """
    Given person info, add skills, languages,hobbies and references parts of the CV.
    """
    top_left_side(p_index, pdf)
    headers = ["Skills Highlights", "Languages", "Hobbies", "References"]
    details = ["skills", "languages", "hobbies", "references"]
    i = 0
    for part in headers:
        current_y = pdf.get_y()
        pdf.set_xy(0, current_y + 10)
        pdf.set_font('Arial', 'B', 11)
        pdf.set_fill_color(0, 0, 0)
        pdf.set_text_color(255, 255, 255)
        pdf.cell(40, 5, part, border=1, ln=2, fill=True)
        pdf.set_font('Arial', 'B', 9)
        info_list = [s.strip() for s in data[details[i]][p_index].split(',')]
        current_y = pdf.get_y()
        pdf.set_xy(3, current_y + 3)
        pdf.set_text_color(0, 0, 0)
        for info in info_list:
            pdf.cell(30, 5, info, ln=2)
        i = i + 1


def main():
    # Create CV for every person in 'data.csv' file
    for p_index in range(len(data)):
        # Create pdf
        pdf = FPDF(format="A4")
        pdf.add_page()

        # ADD template
        img = "templates/temp"+str(p_index+1)+".jpg"
        pdf.image(img, x=0, y=0, w=150, h=297, type='')

        # Add right and left parts
        right_side(p_index, pdf)
        left_side(p_index, pdf)

        # save CV
        pdf.output("CV_outputs/output" + str(p_index+1) + ".pdf")


if __name__ == "__main__":
    main()
