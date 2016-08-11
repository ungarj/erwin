#!/usr/bin/env python3

import sys
import random
import re

FORBIDDEN = '[]()"\''
TRUNC = re.compile('([!?.]+).*')

class Markov:
    def __init__(self, data=None, order=3):
        self.chains = {}
        self.order = order
        if data:
            self.add(data)

    def add(self, data):
        data = ' '.join(data.lower().split())
        for x in FORBIDDEN:
            data = data.replace(x, '')
        for i in range(len(data)):
            key = data[i:i+self.order-1]
            val = data[i+self.order-1:i+self.order]
            if key not in self.chains:
                self.chains[key] = []
            self.chains[key].append(val)
        return self

    def generate(self, max_length=120):
        try:
            current = random.choice(list(self.chains))
            length = 0
            generated = []
            while length < max_length:
                last = current
                current = random.choice(self.chains.get(last, ['']))
                generated.append(current)
                length += len(current)
                if any([x in current for x in '!.?']) or not current:
                    break
                current = (last + current)[1:]
            return TRUNC.sub(
                lambda m: m.group(1),
                ''.join(generated).strip().title().capitalize()
            )
        except:
            return ''


def manfred_sagt(textfile="sample.txt", order=10):
    with open(textfile, 'r') as schas:
        schastext = schas.read()
    return Markov(
        schastext,
        order=order
        ).generate()

if __name__ == '__main__':
    print(manfred_sagt())
