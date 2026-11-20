# Rag_boot.dev
Learning how to build a RAG pipline from scracth


# Preprocessing

keyword search/text processing/ punctuation/ tokenization / stop words / stemming

# Indexing (TF-IDF)

    Steps to Build an Inverted Index:
        *Fetch the Document: Removing of Stop Words: Stop words are the most occurring and useless words in documents like "I", "the", "we", "is", and "an".

        *Stemming of Root Word: Whenever I want to search for "cat", I want to see a document that has information about it. But the word present in the document is called "cats" or "catty" instead of "cat". To relate both words, I'll chop some part of every word I read so that I could get the "root word". There are standard tools for performing this like "Porter's Stemmer".
        
        *Record Document IDs: If the word is already present add a reference of the document to index else creates a new entry. Add additional information like the frequency of the word, location of the word, etc.