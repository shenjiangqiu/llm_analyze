# %%
from transformers import BertModel, BertTokenizer


# %%
model = BertModel.from_pretrained('bert-base-uncased')
print(model)

# %%
