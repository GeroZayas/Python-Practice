---
marp: true
author: Gero Zayas
theme: uncover
class: invert
---

<style>

:root {
    background-color: #cc0000;
  font-family: Arial, sans-serif; /*default font*/
  color: white;
}

h1 {
  color: #ffb600; /*yellow*/
  text-shadow: 2px 2px 10px 0 rgba(0, 0, 0, 0.75); /*drop shadow*/
  font-size: 2em; /*larger font size*/
}

p {
  line-height: 1.6; /*adjusts spacing between lines*/
  font-weight: bold; /*makes the font bolder*/
  color: yellow; /*dark yellow*/
}

/*Add these styles to target elements with the "gold" class*/
.gold {
  background-color: #e6b400; /*goldenrod*/
  color: #333; /*dark gray*/
  border: 1px solid #999; /*medium gray border*/
}
</style>

# Present Perfect Simple
![gif](https://media.giphy.com/media/zU0LX1X7A1Nja/giphy.gif)
Gero Zayas
2023

---

## I *have* done

# You *have* done

### He *has* done

#### We *have* done

---

# Questions

- What have you **done** today?
- Have you ever **been** to Europe?
- What **have** you read about history?
- What **have** you learned recently?

---
This is an Example of **Quick Sort in Python3**
```python
numbers = [12, 93, 67, 68, 53, 7, 25, 40]


# SORT the numbers using quick sort
def quick_sort(nums: list) -> list:
    if len(nums) <= 1:
        return nums
    pivot, left, right = nums[0], [], []

    for num in nums[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)

    return quick_sort(left) + [pivot] + quick_sort(right)


sorted_numbers = quick_sort(numbers)
print("sorted_numbers: ", sorted_numbers)
```

---
