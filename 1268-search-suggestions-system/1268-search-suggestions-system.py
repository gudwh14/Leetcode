class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        answer = []

        left, right = 0, len(products) - 1
        for i in range(len(searchWord)):
            result = []
            word = searchWord[i]

            while left <= right and (len(products[left]) <= i or products[left][i] != word):
                left += 1

            while left <= right and (len(products[right]) <= i or products[right][i] != word):
                right -= 1

            remain = right - left + 1

            for idx in range(min(3, remain)):
                result.append(products[left + idx])
            answer.append(result)
        return answer