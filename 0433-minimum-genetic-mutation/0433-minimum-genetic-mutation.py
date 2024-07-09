class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1
        bank=set(bank)
        queue=deque([(startGene,0)])
        gene_chars = ['A', 'C', 'G', 'T']
        while queue:
            current_gene, mutations = queue.popleft()
            if current_gene==endGene:
                return mutations
            for i in range(len(current_gene)):
                for char in gene_chars:
                    if char!=current_gene[i]:
                        mutated_gene = current_gene[:i] + char + current_gene[i + 1:]
                        if mutated_gene in bank:
                            queue.append((mutated_gene, mutations + 1))
                            bank.remove(mutated_gene) 
        return -1