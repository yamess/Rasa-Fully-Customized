from rasa.model_training import train
from rasa.utils import train_utils
# from rasa.api import train


def train_horoscope_bot(domain_path: str, config_path: str, nlu_data_path: str, model_to_fine_tune: str = None):
    train_result = train(
        domain=domain_path,
        config=config_path,
        training_files=nlu_data_path,
        model_to_finetune=model_to_fine_tune,nlu_additional_arguments={"validation_split":0.2}
    )

    print(train_result)
