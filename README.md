# pythagore

A simple Python utility to work with the Pythagorean theorem.

---

## ✨ Features

- Calculate the hypotenuse from two sides
- Calculate a missing side using the hypotenuse
- Verify if a triangle is right-angled
- Retrieve library metadata (version, creator)

---

## 🔧 Installation

Install via pip:

```bash
pip install pythagore
```

## 🚀 Utilisation

This library is now a simple module (no class required).

Here is an example of using the module :

```python
from pythagore import hypotenuse, adjacent_side, is_rectangle

a = 3
b = 4

h = hypotenuse(a, b)

print("Hypotenuse : ", h)

print("Is right triangle : ", is_rectangle(h, a, b))

missing = adjacent_side(h, a)
print("Missing side : ", missing)
```

example output

```txt
Hypotenuse: 5.0
Is right triangle: True
Missing side: 4.0
```

## 📦 Metadata

You can also access library information:


```python
from pythagore import current_version, creator

print(current_version())
print(creator())
```

example output 

```txt
1.5.0
Creator : Tina
GitHub : https://github.com/Tina-1300
```


## ❗ Prerequisites

- Python >= 3.13.0
- This library uses only the standard library (math)
- No external dependencies required

📄 Licence

This project is distributed under the MIT License.
See the LICENSE file for more information.
[LICENSE](./LICENSE)