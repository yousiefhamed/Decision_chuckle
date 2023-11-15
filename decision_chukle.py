from tkinter import *
from tkinter import messagebox, ttk, simpledialog

class DecisionChukle:
    def __init__(self):
        self.root = Tk()
        self.root.title("DecisionChukle - Serious Risk, Seriously fun 😂")
        self.root.geometry("720x720")
        self.root.configure(bg="#F4F4F4")  # Set background color

        # list of the criteria that a user can use
        # to solve the problem case
        self.criteria = [
            {
                'criteria': 'Maximax (optimistic)',
                'method': self.maximax
            },
            {
                'criteria': 'Maximin (pessimistic)',
                'method': self.maximin
            },
            {
                'criteria': 'Criterion of Realism (Hurwicz)',
                'method': self.criterionOfRealism
            },
            {
                'criteria': 'Equally Likely (Laplace)',
                'method': self.equallyLikely
            },
            {
                'criteria': 'Minimax Regret',
                'method': self.minimaxRegret
            },
        ]

        # Inputs that a user has to Enter
        self.noOfAlternatives = IntVar()
        self.noOfStateOfNatures = IntVar()
        self.chosenCriteria = StringVar()
        self.numbersOfInputs = []
        self.noOfAlphas = IntVar()
        self.alphaValues = []

        # Result 
        self.result = IntVar()
        self.alternative = IntVar()

        self.create_widgets()
        self.root.mainloop()

    def create_widgets(self):
        self.create_header()
        self.create_input_fields()

    def create_header(self):
        header = Frame(self.root, bg="#009688")
        header.grid(sticky="ew")

        Label(header, text="Decision Making Under Uncertainty", fg="white", bg="#009688", font=("Arial", 16)).grid(pady=10)
        Label(header, text="Supervised by Dr. Abeer & Dr. Nourhan", fg="white", bg="#009688").grid()

    def create_input_fields(self):
        input_fields = Frame(self.root, bg="#F4F4F4")
        input_fields.grid(pady=20)

        criteria_labels = Label(input_fields, text="Enter Criteria:", font=("Arial", 12), bg="#F4F4F4")
        criteria_labels.grid(sticky="w", pady=5)

        criteria_combobox = ttk.Combobox(input_fields, textvariable=self.chosenCriteria, values=[criteria['criteria'] for criteria in self.criteria], font=("Arial", 12))
        criteria_combobox.grid(sticky="w", pady=5)

        alternatives_label = Label(input_fields, text="Number of Alternatives:", font=("Arial", 12), bg="#F4F4F4")
        alternatives_label.grid(sticky="w", pady=5)
        alternatives_entry = Entry(input_fields, textvariable=self.noOfAlternatives, font=("Arial", 12), width=5)
        alternatives_entry.grid(sticky="w", pady=5)

        state_of_natures_label = Label(input_fields, text="Number of State of Natures:", font=("Arial", 12), bg="#F4F4F4")
        state_of_natures_label.grid(sticky="w", pady=5)
        state_of_natures_entry = Entry(input_fields, textvariable=self.noOfStateOfNatures, font=("Arial", 12), width=5)
        state_of_natures_entry.grid(sticky="w", pady=5)

        start_button = Button(input_fields, text="Let's Have Fun 😄", command=self.getPredictionNumbers, bg="#009688", fg="white", font=("Arial", 12))
        start_button.grid(pady=10)

    def chooseCriteria(self):
        try:
            for index, criteria in enumerate(self.criteria):
                if criteria['criteria'] == self.chosenCriteria.get():
                    criteria['method']()
                    return
            messagebox.showerror(title="Error😵", message=f"This Criteria is not Supported yet 🫠")
            return
        except Exception as e:
            messagebox.showerror(title="Error😵", message=f"Error During Choosing a Criteria 🥴: {e}")

    def getPredictionNumbers(self):
        try:
            if int(self.noOfAlternatives.get()) < 2 or int(self.noOfStateOfNatures.get()) < 1:
                messagebox.showerror(title="Error 😵", message="The Number of Alternatives have to be 2 at least & \nThe Number of State of Natures have to be 1 at least")
                return

            if hasattr(self, "getInputs"):
                keepNumbers = messagebox.askyesno(title="Keep Numbers", message="Do you want to keep the same numbers? 🤔")
                if not keepNumbers:
                    self.getInputs.destroy()
                    self.numbersOfInputs = []
                else:
                    self.chooseCriteria()
                    return

            self.getInputs = Frame(self.root, bg="#F4F4F4")  # Set background color
            self.getInputs.grid(pady=20)  # Add padding

            try:
                if self.noOfAlternatives.get() and self.noOfStateOfNatures.get():
                    Label(self.getInputs, text="State of Natures", font=("Arial", 14), bg="#F4F4F4").grid(pady=10)

                    # Create table headers
                    Label(self.getInputs, text="Alternative", font=("Arial", 12, "bold"), bg="#F4F4F4").grid(row=1, column=0, padx=5)
                    for stateOfNature in range(self.noOfStateOfNatures.get()):
                        Label(self.getInputs, text=f"Nature {stateOfNature + 1}", font=("Arial", 12, "bold"), bg="#F4F4F4").grid(row=1, column=stateOfNature + 1, padx=5)

                    # Create table cells
                    for alternative in range(self.noOfAlternatives.get()):
                        self.numbersOfInputs.append([])
                        Label(self.getInputs, text=f"Alt {alternative + 1}", font=("Arial", 12), bg="#F4F4F4").grid(row=alternative + 2, column=0, padx=5)
                        for stateOfNature in range(self.noOfStateOfNatures.get()):
                            entry_var = IntVar()
                            self.numbersOfInputs[alternative].append(entry_var)
                            Entry(self.getInputs, textvariable=entry_var, font=("Arial", 12), width=5).grid(row=alternative + 2, column=stateOfNature + 1, padx=5)

                    Button(self.getInputs, text="Decision Chukle", command=self.chooseCriteria, bg="#009688", fg="white", font=("Arial", 12)).grid(pady=10)
            except Exception as e:
                messagebox.showwarning(title='Warning⚠️', message=f"Something went wrong while getting Predictions Numbers: {e}")

        except Exception as e:
            messagebox.showerror(title="Error 😵", message=f"{e}")

    def maximax(self):
        maximumsOfStates = []

        for index, alternatives in enumerate(self.numbersOfInputs, start=0):
            maximumsOfStates.append([])
            for state in alternatives:
                maximumsOfStates[index].append(state.get())

            maximumsOfStates[index] = (max(maximumsOfStates[index]))

        self.result.set(max(maximumsOfStates))
        self.alternative.set(maximumsOfStates.index(max(maximumsOfStates)) + 1)

        self.getResult("a Payoff")

    def maximin(self):
        minimumOfStates = []

        for index, alternatives in enumerate(self.numbersOfInputs, start=0):
            minimumOfStates.append([])
            for state in alternatives:
                minimumOfStates[index].append(state.get())

            minimumOfStates[index] = (min(minimumOfStates[index]))

        self.result.set(max(minimumOfStates))
        self.alternative.set(minimumOfStates.index(max(minimumOfStates)) + 1)

        self.getResult("a Payoff")

    def criterionOfRealism(self):
        self.noOfAlphas.set(0)
        self.alphaValues = []

        ignoringStatesOfNature = []

        min_value = 2
        max_value = self.noOfStateOfNatures.get()

        # Ask for the user's choice on how to enter alpha values
        alphaEntryType = messagebox.askquestion("Alpha Entry", "How would you like to enter alpha values?\n\nClick 'Yes' to enter alphas for all state of natures, \n\n'No' to ignore some state of natures")

        if alphaEntryType == 'yes':
                noOfAlpha = self.noOfStateOfNatures.get()

                for index, alpha in enumerate(range(noOfAlpha), start=1):
                    alphaValue = simpledialog.askfloat("Ask for α", f"value no. {index}: Enter the α value between 0 and 1", minvalue=0, maxvalue=1)

                    if alphaValue is None:
                        return

                    self.alphaValues.append(alphaValue)

        elif alphaEntryType == 'no':
            # Case 2: User wants to enter all alpha values except the last one

            if self.noOfStateOfNatures.get() < 3:
                min_value = 1

            noOfAlpha = simpledialog.askinteger("Ask for α", f"Enter the number of α between {min_value} and {max_value - 1}", minvalue=min_value, maxvalue=max_value - 1)

            if noOfAlpha is None:
                return
            
            messagebox.showwarning("Warning", f"You have to Ignore {max_value - noOfAlpha} state of natures")
            for index, ignore in enumerate(range(max_value - noOfAlpha), start=1):
                while True:
                    ignoringStates = simpledialog.askinteger("Ignoring State of Nature", f"Enter the Ignoring state of nature no. {index} of {max_value - noOfAlpha}", minvalue=1, maxvalue=max_value)
                    if ignoringStates not in ignoringStatesOfNature:
                        ignoringStatesOfNature.append(ignoringStates)
                        break
                    else:
                        messagebox.showwarning("Duplicate Entry", "You have already entered this state. Please choose a different one.")
            
            for index, alpha in enumerate(range(noOfAlpha), start=1):
                alphaValue = simpledialog.askfloat("Ask for α", f"value no. {index}: Enter the α value between 0 and 1", minvalue=0, maxvalue=1)

                if alphaValue is None:
                    return

                self.alphaValues.append(alphaValue)
            
        else:
            messagebox.showwarning("Warning ⚠️", "Invalid choice for alpha entry. Please try again.")
            return

        # Check if the sum of alpha values is equal to 1
        if sum(self.alphaValues) != 1:
            messagebox.showwarning("Warning ⚠️", "Sum of alphas should be equal to 1. Please try again.")
            self.criterionOfRealism()
        else:
            matrix = []
            
            for index, alternative in enumerate(self.numbersOfInputs, start=0):
                matrix.append([])
                for selectedState, state in enumerate(alternative, start=0):
                    if selectedState + 1 not in ignoringStatesOfNature:
                        matrix[index].append(state.get() * self.alphaValues[selectedState])
                matrix[index] = sum(matrix[index])
                
        self.result.set(max(matrix))
        self.alternative.set(matrix.index(max(matrix)) + 1)

        self.getResult("a Payoff")

    def equallyLikely(self):
        averageMatrix = []

        for index, alternative in enumerate(self.numbersOfInputs, start=0):
            averageMatrix.append([])
            for state in alternative:
                averageMatrix[index].append(state.get())
            averageMatrix[index] = sum(averageMatrix[index]) / len(averageMatrix[index])

        self.result.set(max(averageMatrix))
        self.alternative.set(averageMatrix.index(max(averageMatrix)) + 1)

        self.getResult("a Payoff")

    def minimaxRegret(self):
        matrix = []

        for index, alternative in enumerate(self.numbersOfInputs, start=0):
            matrix.append([])
            for selectedState, state in enumerate(alternative, start=0):
                matrix[index].append(state.get())

        # Transpose the matrix
        transposed_matrix = list(map(list, zip(*matrix)))

        bestPayoffs = [max(state) for state in transposed_matrix]

        for index, alternative in enumerate(self.numbersOfInputs, start=0):
            for selectedState, state in enumerate(alternative, start=0):
                matrix[index][selectedState] = bestPayoffs[selectedState] - state.get()
            matrix[index] = max(matrix[index])

        self.result.set(min(matrix))
        self.alternative.set(matrix.index(min(matrix)) + 1)

        self.getResult("an Opportunity loss")

    def getResult(self, returnValue):
        try:
            if hasattr(self, "showResult"):
                self.showResult.destroy()
                
            result = self.result.get()
            alternative = self.alternative.get()

            self.showResult = Frame(self.root)
            self.showResult.grid()

            Label(self.showResult, text=f'The Best Alternative is No.{alternative} with {returnValue} = {result}', font=("Arial", 15, "bold")).grid()
        except Exception as e:
            messagebox.showerror(title="Error 😵", message=f"{e}")

if __name__ == "__main__":
    DecisionChukle()
