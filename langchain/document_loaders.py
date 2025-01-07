from langchain_community import document_loaders

loader = document_loaders("windows_base_vm_image_create_steps.md")
loader.load()

# from langchain.document_loaders.csv_loader import CSVLoader

loader = document_loaders('skip_models.csv')
data = loader.load()

#自定义解析
loader = document_loaders(file_path='documents, index.csv', csv_args={
    'delimiter': ',',
    'quotecher': '"',
    'fieldnames': ['title', 'context']
})
data = loader.load()

