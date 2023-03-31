import os
import openai
import config
openai.api_key = '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'

def openAI(query):
        response=openai.Completion.create(
            model="text-davinci-003",
            prompt=query,
            temperature=0.5,
            max_tokens=200,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        if 'choices' in response:
            if len(response['choices']) > 0:
                answer = response['choices'][0]['text']
            else:
                answer = 'Sorry! The AI could not understand what you are looking for'
        else:
            answer = 'Sorry! The AI could not understand what you are looking for'
        '''print(answer)'''
        return answer


