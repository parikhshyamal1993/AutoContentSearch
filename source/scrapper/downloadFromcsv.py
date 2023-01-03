
import requests
import os

headers = {
        "User-Agent": "Chrome/51.0.2704.103",
    }

def DownloadAnnualreport(url,des):
    response = requests.get(url,headers=headers)
    pdfName = url.split('/')[-1]
    pdfDump = os.path.join(des,pdfName)
    #os.remove(pdfDump)
    with open(pdfDump, 'wb') as f:
       f.write(response.content)

    return "success"


def DownLoaderApplicaiton(csvFile,destination):
    with open(csvFile,'r') as f:
        lines = f.readlines()
        for line in lines:
            url = line.split(",")[0]
            print(url)
       
            
            DownloadAnnualreport(url,destination)
            #\exit()
if __name__=="__main__":

    filePath = "../../assets/links.csv"
    destination = "../../assets/TestData/"
    DownLoaderApplicaiton(filePath,destination)
