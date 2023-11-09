import shelve
import os


def write_shelve(file_path, data):
    f = shelve.open(file_path)
    for i, problem in enumerate(data):
        f[str(i)] = problem


def read_shelve(file_path):
    f = shelve.open(file_path)

    for i in f:
        print(f[i])


if __name__ == '__main__':
    path = os.getcwd()
    file_path = os.path.join(path, "problem_db")

    prob = [{"title": "An Episode You Can't Refuse"},
            {"category": "On the Run With a Mammal",
             "question": "Let's say you turn state's evidence and need to \"get on the lamb.\" If you wait too long, "
                         "what will happen?",
             "answer": ["You'll end up on the sheep",
                        "You'll end up on the cow",
                        "You'll end up on the goat",
                        "You'll end up on the emu"],
             "correct": 1,
             "explanation": "\"you'll end up on the sheep,\" humorously reinterprets the phrase \get on the lamb\" "
                            "to suggest that if you don't escape and instead wait, you will be caught by law "
                            "enforcement, depicted metaphorically as \"sheep.\""},
            {"category": "math",
             "question": "(4/2^(√2))^(2 + √2)",
             "answer": ["1/4",
                        "1/2",
                        "2",
                        "4"],
             "correct": 4,
             "explanation": "= (2^2 / 2^(√2))^(2 + √2)\n= (2^(2 - (√2)))^(2 + (√2))"
                            "\n= 2^(2 - (√2)) * (2 + (√2))\n= 2^(4 - 2)\n= 2^2\n= 4"},
            {"category": "What is the most appropriate change of mind for Jonas revealed in the following article?",
             "question": "Looking out the bus window, Jonas could not stay calm. He had been looking forward to this "
                         "field trip. It was the first field trip for his history course. His history professor had "
                         "recommended it to the class, and Jonas had signed up enthusiastically. He was the first to "
                         "board the bus in the morning. The landscape looked fascinating as the bus headed to Alsace. "
                         "Finally arriving in Alsace after three hours on the road, however, Jonas saw nothing but "
                         "endless agricultural fields. The fields were vast, but hardly appealed to him. He had "
                         "expected to see some old castles and historical monuments, but now he saw nothing like that "
                         "awaiting him. \"What can I learn from these boring fields?\" Jonas said to himself with a "
                         "sigh.",
             "answer": ["excited → disappointed",
                        "indifferent → thrilled",
                        "amazed → horrified",
                        "surprised → relieved"],
             "correct": 1,
             "explanation": "Through the phrase 'had been looking forward,' you can sense the anticipation, "
                            "but in the last part, \"he saw nothing like that awaiting him\" conveys the "
                            "disappointment of finding nothing waiting for him. so the correct answer is 1."},
            {"category": "nonsense",
             "question": "Why was 6 afraid of 7?",
             "answer": ["123",
                        "345",
                        "678",
                        "617"],
             "correct": 3,
             "explanation": "It's a play on words where \"ate\" sounds like the number 8, suggesting that 7 has eaten "
                            "9, which is a humorous and nonsensical twist."},
            {"category": "nonsense",
             "question": "What is always coming, but never arrives?",
             "answer": ["Today",
                        "Last week",
                        "Yesterday",
                        "Tomorrow"],
             "correct": 4,
             "explanation": "Tomorrow is a concept of the future that is always just one day away but never actually "
                            "arrives because once it does, it becomes \"today\""}
            ]

    write_shelve(file_path, prob)
    read_shelve(file_path)
