#あるフォルダーに入ったファイル（ただし、ファイル名は○○_□□という形式である必要がある）を分類するプログラム
import os
import shutil

#一つ目の関数。元フォルダーの中身を振り分け用のフォルダーに移動させる
def move_files_to_output_folder(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)
        if os.path.isfile(file_path):
            dest_path = os.path.join(output_folder, filename)

            shutil.move(file_path, dest_path)

            print(f" '{filename}' を '{output_folder}'に移動しました。" )

#二つ目の関数。振り分け用のフォルダーに含まれるファイルを分類する
def classify_files_by_course(output_folder):
    for filename in os.listdir(output_folder):
        file_path = os.path.join(output_folder, filename)
        if os.path.isfile(file_path):
            if '_' in filename:
                course_name   = filename.split('_')[0]
                course_folder = os.path.join(output_folder, course_name)
                os.makedirs(course_folder, exist_ok = True)

                dest_path = os.path.join(course_folder, filename)
                shutil.move(file_path, os.path.join(course_folder, filename))

                print(f"'{filename}' を '{course_name}' に移動しました。")
            else:
                print(f"error:Skipped '{filename}' - ファイル名が適切ではありません。「○○_□□」という名前のフォルダにしてください。")

move_files_to_output_folder(r'C:\Users\sunsh\OneDrive\デスクトップ\program\py\fileApp\ファイル入れ', r'C:\Users\sunsh\OneDrive\デスクトップ\program\py\fileApp\出力結果')
classify_files_by_course(r'C:\Users\sunsh\OneDrive\デスクトップ\program\py\fileApp\出力結果')