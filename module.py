from transformers import BertTokenizer, EncoderDecoderModel

tokenizer = BertTokenizer.from_pretrained(
    "cahya/bert2bert-indonesian-summarization")
tokenizer.bos_token = tokenizer.cls_token
tokenizer.eos_token = tokenizer.sep_token
model = EncoderDecoderModel.from_pretrained(
    "cahya/bert2bert-indonesian-summarization")

kwargs = {
    "max_length": 200,
    "num_beams": 2,
    "repetition_penalty": 2.5,
    "length_penalty": 1.0,
    "early_stopping": True,
    "no_repeat_ngram_size": 5,
    "use_cache": True
}


def summarize(text):
    input_text = tokenizer.encode(text, return_tensors='pt')
    summary = model.generate(input_text, **kwargs)
    summary_text = tokenizer.decode(summary[0], skip_special_tokens=True)
    return summary_text
