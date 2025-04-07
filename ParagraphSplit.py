import pandas as pd
import re

# Paste text into the paragraph variable
# This is a sample text from a speech by the Prime Minister of India, Narendra Modi, at the UN General Assembly in 2014.
paragraph = """Mr. President and Distinguished Delegates,

Let me first congratulate you on your election as the President of the 69th session of United Nations General Assembly.

It is truly a great honour to address you for the first time as the Prime Minister of India. I stand here conscious of the hopes and expectations of the people of India.

I am also mindful of the expectations of the world from 1.25 billion people.

India is a country that constitutes one-sixth of humanity; a nation experiencing economic and social transformation on a scale rarely seen in history.

Every nation's world view is shaped by its civilization and philosophical tradition. India's ancient wisdom sees the world as one family.

It is this timeless current of thought that gives India an unwavering belief in multilateralism.

Today, as I stand here, I am equally aware of the hopes that are pinned on this great assembly. I am struck by the sacred belief that brought us together.

An extraordinary vision and a clear recognition of our shared destiny brought us together to build this institution for advancing peace and security, the rights of every human being and economic development for all. From 51 nations then, today 193 sovereign flags fly at this hope.

We have achieved much in the past six decades in our mission in ending wars, preventing conflict, maintaining peace, feeding the hungry, striving to save our planet and creating opportunities for children. 69 UN peacekeeping missions since 1948 have made the blue helmet the colour of peace.

Today, there is a surge of democracy across the world; including in South Asia; in Afghanistan, we are at a historic moment of democratic transition and affirmation of unity. Afghans are showing that their desire for a peaceful and democratic future will prevail over violence. Nepal has moved from violence to peace and democracy; Bhutan's young democracy is flourishing. Democracy is trying to find a voice in West Asia and North Africa; Tunisia's success makes us believe that it is possible.

There is a new stirring for stability, progress and prosperity in Africa. There is unprecedented spread of prosperity in Asia and beyond, rising on the strength of peace and stability. Latin America, a continent of enormous potential, is coming together in shared pursuit of stability and prosperity, which could make it an important anchor of the world.

Today, the United Nations is celebrating its 70th anniversary. This is a great occasion to reflect and to reform—to look within and beyond, so that the United Nations remains relevant and effective in the 21st century.

Institutions that reflect the imperatives of the 20th century won't be effective in the 21st. They must be built on the foundation of democracy and participation; they must empower nations and people; and they must become more representative and inclusive.

The need for reform in the United Nations and its Security Council has been recognized widely. We must fulfil it in a fixed time frame. The next year should be an opportunity of this.

We must reform the United Nations, including the Security Council, and make it more democratic and participative.

This will increase the United Nations’ credibility and effectiveness in addressing the challenges of our time.

Mr. President,

The world is witnessing tensions and turmoil on a scale rarely seen in recent times. The fault lines are shifting from the boundaries of nations into the web of our societies and the streets of our cities.

In many parts of the world, the problems arise out of the vacuum of development and absence of good governance; they are also not new. But, we tend to focus on them only when they emerge as crises.

We must understand that these are merely symptoms; we must address the root causes. Peace and stability are not enough; they must be underpinned by economic progress and human welfare.

A life of dignity begins with the basic necessities of life: clean water and sanitation; shelter and education; affordable health care and access to clean energy.

For the first time, India is close to ensuring basic sanitation in every home. We will soon launch a Clean India Mission. We will build modern toilets in every school in less than a year.

We have set up a new ministry for skill development. We will provide the youth the capability to realize their potential: a job or self-employment; a life of purpose and dignity.

We will launch a campaign for Digital India. We will connect our villages with broadband. We will make our schools and institutions world class.

We will provide a roof over every head and electricity to all households.

I know it is ambitious. But, we live in an age of great opportunities. And, India is blessed with the extraordinary human capital of 800 million youth.

We are prepared to learn from others, and share our experiences.

We will work with the world to achieve that future.

When we dream of a Digital India, we are not just seeking to make our future, but also build the bridge across the digital divide.

When we launch a Clean India Mission, we aim not only to improve the well-being of our people, but also reduce the toll on our environment.

We will pursue development that is socially inclusive and environmentally sustainable.

Mr. President,

India's traditional support to UN peacekeeping reflects its commitment to the United Nations.

India has contributed troops to most of the UN peacekeeping missions. We will always be there to contribute.

We must also ensure that the capacity of United Nations peacekeeping and the safety of peacekeepers are enhanced.

As a nation with a long-standing tradition of spiritualism and a society with deep cultural roots, India is committed to promoting peace and harmony. Terrorism has no religion. Terrorism uses diverse motivations and causes, none of which justify it. Terrorism must be delinked from religion. To believe otherwise is to give it a legitimacy that it does not deserve and will be counter-productive.

We should not forget that when we provide shelter to terrorists, we nurture them at our own peril. And those using terrorism as instrument of their policy must understand that it is an instrument that is not only futile but also self-destructive.

Mr. President,

Let us work together to ensure that the future belongs not to those who seek to destroy but to those who build and create.

Let us unite against terrorism and give meaning to the call for a UN Comprehensive Convention on International Terrorism.

Mr. President,

I also want to say that we need to intensify dialogue and engagement between countries. We must ensure that our conversations are purposeful, because they hold the key to the future we wish for.

This is why I am here. I want to hold dialogue with all those who want to shape the world in a positive way.

In this world of interdependence, isolation is not a solution.

We must build bridges—bridges that connect aspirations of people and unite the world.

"""

def split_paragraph(paragraph):
    paragraph_num = 1

    # Split paragraphs using double newline
    paragraph_list = paragraph.split("\n\n")
    abbreviations = ['Mr.', 'Mrs.', 'Dr.', 'Ms.', 'Prof.', 'Rev.', 'St.', 'e.g.', 'i.e.', 'etc.', 'vs.']

    cleaned = []

    for paragraph in paragraph_list:
        if paragraph.strip():
            temp_paragraph = paragraph
            for abbr in abbreviations:
                temp_paragraph = temp_paragraph.replace(abbr, abbr.replace('.', 'PERIOD_MARKER'))
            temp_paragraph = re.sub(r'(\d+)\.(\d+)', r'\1DECIMAL_MARKER\2', temp_paragraph)

            sentences = temp_paragraph.split('.')

            processed_sentences = []
            for s in sentences:
                if s.strip():
                    s = s.replace('PERIOD_MARKER', '.')
                    s = s.replace('DECIMAL_MARKER', '.')
                    s = s.strip()
                    if(s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'")):
                        s = s[1:-1]
                    processed_sentences.append(s)
            for sentence in processed_sentences:
                cleaned.append({'Paragraph': paragraph_num, 'Sentence': sentence.strip()})
            paragraph_num += 1
    df = pd.DataFrame(cleaned)
    return df

cleaned_df = split_paragraph(paragraph)
print(cleaned_df)
# Save to Excel file, change the name as needed
cleaned_df.to_excel('paragraph_split.xlsx', index=False)
# The code above splits the given paragraph into sentences and saves them into a excel file.