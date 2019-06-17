import os

def output2excel(file_dir):
    if os.path.exists(file_dir):
        file_writer = open(os.path.join(file_dir, "result.csv"), "w")
        file_dirs = os.listdir(file_dir)
        for i in range(0, len(file_dirs)):
            path_dir = os.path.join(file_dir, file_dirs[i])
            if os.path.isfile(path_dir):
                continue
            imgs = os.listdir(path_dir)
            file_writer.write("{},{}\n".format(file_dirs[i], len(imgs)))
        file_writer.close()

file_dir = 'F:/图片抽样检测/2019-05-10/异常图片'
output2excel(file_dir)
