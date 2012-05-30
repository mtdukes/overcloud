import sys, urllib2, argparse, csv
import simplejson as json

def get_urls(json_path):
    
    source_data = open(json_path).read()
    print '...json data acquired'
    project_data = json.loads(source_data) ##parse json
    print '...json parsing complete'
    documents = project_data['documents']
    writer = csv.writer(open('{0}.csv'.format(json_path.replace('.','-')), 'wb'))
    writer.writerow(['uid','text','url'])
    for d in documents:
        try:
            if d['access'] != 'public' :
                continue
            print d['canonical_url'] ##checks on capture progress
            r = d.get('resources', {})
            text_file = r.get('text','no file found')
            text_data = urllib2.urlopen(text_file).read() 
            uid = d.get('id', '')
            url = d.get('canonical_url', '')
            writer.writerow([uid, text_data, url])
        except:
            print 'ERROR: '
            print d['id']
    print '...done'

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Process a file')
    parser.add_argument('file', help='Enter the path of the JSON file')
    args = parser.parse_args()
    
    get_urls(args.file)
    print 'Please proceed to Overview.'