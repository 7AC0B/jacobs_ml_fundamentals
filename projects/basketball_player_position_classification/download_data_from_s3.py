import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..', '..'))
sys.path.append(project_root)

from utils.s3_helpers import save_csvs_from_s3_to_folder

save_csvs_from_s3_to_folder(
    bucket='jacobs-projects',
    prefix='datasets/basketball_player_data/',
    save_to_path = 'projects/basketball_player_position_classification/data'
)

print('Successfully saved data from S3.')