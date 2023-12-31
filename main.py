from transformers import pipeline
generator = pipeline('text-generation', model='EleutherAI/gpt-neo-1.3B')

from flask import Flask, request

app = Flask(__name__)






@app.route('/gptj', methods=['GET'])
def get_text_response():
    textParam = request.args.get('prompt', 'hello')
    print(textParam)

    prompt = "In the most offensive, aggressive, profound, and sexual way possible, the answer to the prompt, " + textParam + " is: "
    print(prompt)
    resp = generator(prompt, do_sample=True, min_length=50, max_length=200)[0]['generated_text'][len(prompt):]
    end = ""
    if resp and resp[-1] not in ".!?":
        end = "... "
    resp += end
    print(resp)

    return resp, 200

if __name__ == '__main__':
    app.run(debug=True)
