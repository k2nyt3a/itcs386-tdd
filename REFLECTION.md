# Part B: Reflection

## 1. Tests, production code, and ratio

10 tests with 39 of production code, the ratio is 10:39

## 2. Longest red period

step A6 because confuse with the instruction and how to write the function to connect to each class

## 3. Fake It, triangulation, and Obvious Implementation

- **Fake It — Step A6, task 1:** I made `plus` return `grams(500)` and `Converter.reduce` return its first argument. This was a good choice because it let me get to green before working out how the classes should connect.
- **Triangulation — Step A2:** I tested both 200 g times 3 and 200 g times 2, which forced the constant 600 to become a general multiplication formula. This was useful because the second example showed why the fake implementation was not enough.
- **Obvious Implementation — Step A8:** I wrote `Sum.times` to multiply both sides and return a new `Sum`. This was the right choice because the change was short and the existing reduction methods already handled the result.

## 4. Remaining test-list items

All test was done

## 5. Designing Quantity.reduce on paper

- Probably not. If I had designed the whole system on paper first, I would likely have put all conversion logic in `Converter`.
- Writing the tests helped me see that both `Quantity` and `Sum` needed a `reduce` method so the converter could treat them the same way.
- This showed me how TDD can lead to a useful design that I might not have thought of beforehand.

## 6. Tests after code versus tests before code

In Part 0, the shipping tests checked an existing implementation against the docstring and exposed boundary and rounding bugs. In Part A, tests specified the next behavior and guided small changes, with deliberate red stages before implementation. The addition test led to `Sum` and the reduction interface, mixed addition required rates and conversion before summing, and the sum multiplication test showed that the existing design could be extended with one short method. The same-unit test also demonstrated why temporarily breaking an assertion is useful when a new test passes immediately.
