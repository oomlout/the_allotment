import os




def main(**kwargs):
    sync(**kwargs)




def sync(**kwargs):    
    following = []
    with open('follow', 'r') as f:
        following = f.read().splitlines()

    if not os.path.exists('data'):
        os.makedirs('data')

    for follow in following:        
        if '/' not in follow:
            follow = f"{follow}/the_allotment_{follow}"
        user = follow.split('/')[0]
        host = "github.com"
        url_repo = f"https://{host}/{follow}"
        dir_follow = "data/follow"
        dir_user = f"{dir_follow}/{host}/{user}"
        dir_full = f"{dir_follow}/{host}/{follow}"
        if not os.path.exists(dir_user):
            os.makedirs(dir_user)
        
        try:
            if not os.path.exists(dir_full):
                #clone into data folder
                os.chdir(dir_user)
                os.system(f'git clone {url_repo}')
                os.chdir('/')
            else:
                #pull from data folder
                os.chdir(dir_full)
                os.system('git pull')
                os.chdir('/')
        except Exception as e:
            print(f"Error syncing {follow}")
            print(e)



if __name__ == '__main__':
    main()