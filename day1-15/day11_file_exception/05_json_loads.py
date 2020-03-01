
import json
import requests

def main():
    response = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
    data_model  =json.loads(response.text)
    print(data_model)
    # for news in data_model['newlist']:
    #     print(news['title'])

if __name__ == '__main__':
    main()