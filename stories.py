"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, story_id, description, words, text,):
        """Create story with words and template text."""

        self.story_id = story_id
        self.description = description
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started
story001 = Story('001',
                 'Once upon a time...',
                 ["place", "noun", "verb", "adjective", "plural noun"],
                 """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural noun}."""
                 )

# STORY TEMPLATE FROM:
# https://thoughtcatalog.com/january-nelson/2018/06/funny-stories/
# accessed: 2/12/2021

story002 = Story('002',
                 'A Date to Forget',
                 ['name', 'place', 'noun-1', 'noun-2',
                  'verb(ing)-1', 'noun-3', 'body part-1', 'noun-4', 'verb(ing)-2', 'body part-2', 'possessive pronoun'],
                 """In my junior year of high school, {name} asked me on a date to {place}. {name} rented a {noun-1} and we made a {noun-2}. We were {verb(ing)-1} the {noun-1} and the {noun-3} beeped so the {noun-2} was done. {name} looked me dead in the eye and said, “This is the worst part.” I then watched {name} open the {noun-3} and pull the {noun-2} out with {possessive pronoun} bare {body part-1}, {noun-4} and all, {verb(ing)-2} at the top of his {body part-2}. We never had a second date."""
                 )

story003 = Story('003',
                 'the Failing Student',
                 ['fraction', 'adjective', 'noun-1', 'noun-2', 'verb-1', 'verb-2',
                     'family member', 'emotion', 'possessive pronoun', 'plural noun'],
                 'I failed the first {fraction} of a class in middle school, so I made a {adjective} {noun-1}. I did this every {fraction} that year. I forgot that they {verb-1} home the end-of-year {noun-1}s, and my {family member} got it before I could {verb-2} with my {adjective} one. My {family member} was {emotion}—at the school for their error. The {noun-2} also retired that year and had already thrown out {possessive pronoun} {plural noun}, so they had to take my {family member}’s “{noun-1}” (the {adjective} ones I made throughout the year) and “correct” the “mistake.” I’ve never told {subject pronoun} the truth.')

STORIES = [story001, story002, story003]


dict_stories_by_id = {story.story_id: story for story in STORIES}
