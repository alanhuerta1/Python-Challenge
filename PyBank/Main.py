{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Import\n",
    "\n",
    "import os \n",
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {},
   "outputs": [],
   "source": [
    "#create path to file\n",
    "\n",
    "PyBank_path = os.path.join (\"Resources/budget_data-Copy1.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Open your file\n",
    "\n",
    "with open(PyBank_path) as csvfile:\n",
    "    csvreader = csv.reader(csvfile,delimiter = ',')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Read file and delimit\n",
    "\n",
    "with open(PyBank_path) as csvfile:\n",
    "    csvreader = csv.reader(csvfile,delimiter = ',')\n",
    "    \n",
    "    #the variables?\n",
    "    \n",
    "    months=0\n",
    "    revenue=0\n",
    "    \n",
    "    #Count the Total Rows\n",
    "    \n",
    "    rows = [r for r in csvreader]\n",
    "    \n",
    "    #Defaulting to the First Value available in the Sheet\n",
    "    \n",
    "    change_revenue = int(rows[1][1])\n",
    "    max = rows[1]\n",
    "    min = rows[1]\n",
    "    \n",
    "    #Loop\n",
    "    \n",
    "    for i in range(1,len(rows)):\n",
    "        \n",
    "        months = months + 1\n",
    "        row = rows[i]\n",
    "        revenue = int(row[1]) + revenue\n",
    "    \n",
    "        #no header Header Row\n",
    "        if i > 1:\n",
    "           change_revenue = change_revenue + int(row[1])-int(rows[i-1][1])\n",
    "            \n",
    "        #Max Revenue\n",
    "        if int(max[1]) < int(row[1]):\n",
    "            max = row\n",
    "            \n",
    "        #Min Revenue\n",
    "        if int(min[1]) > int(row[1]):\n",
    "            min = row\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Financial Analysis\n",
      "------------------\n",
      "Total Months: -86\n",
      "Total Revenue: $38382578\n",
      "Average Revenue Change: $-446309\n",
      "Average Change in Revenue Change: $-7803\n",
      "Greatest Increase in Revenue:Feb-2012 ($1170593)\n",
      "Greatest Decrease in Revenue:Sep-2013 ($-1196225)\n"
     ]
    }
   ],
   "source": [
    "#Calculating Average and Average Change in Revenue\n",
    "average = int(revenue / months)\n",
    "average_change_revenue = int(change_revenue/months)\n",
    "\n",
    "#Printing the Outputs\n",
    "print(\"Financial Analysis\")\n",
    "print(\"------------------\")\n",
    "print(\"Total Months: \" + str(months))\n",
    "print(\"Total Revenue: \" +\"$\" +str(revenue))       \n",
    "print(\"Average Revenue Change: \" +\"$\"+ str(average))\n",
    "print(\"Average Change in Revenue Change: \" +\"$\"+ str(average_change_revenue))\n",
    "print(\"Greatest Increase in Revenue:\" + str(max[0])+\" ($\" + str(max[1])+\")\")\n",
    "print(\"Greatest Decrease in Revenue:\" + str(min[0])+\" ($\" + str(min[1])+\")\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Financial Analysis\n",
      "------------------\n",
      "Total Months: 86\n",
      "Total Revenue: $38382578\n",
      "Average Change: $446309\n",
      "Average Change in Revenue Change: $7803\n",
      "Greatest Increase in Revenue:Feb-2012 ($1170593)\n",
      "Greatest Decrease in Revenue:Sep-2013 ($-1196225)\n"
     ]
    }
   ],
   "source": [
    "#Calculating Average and Average Change in Revenue\n",
    "average = int(revenue / months)\n",
    "average_change_revenue = int(change_revenue/months)\n",
    "\n",
    "#Printing the Outputs\n",
    "print(\"Financial Analysis\")\n",
    "print(\"------------------\")\n",
    "print(\"Total Months: \" + str(months))\n",
    "print(\"Total Revenue: \" + \"$\" +str(revenue))       \n",
    "print(\"Average Change: \" +\"$\"+ str(average))\n",
    "print(\"Average Change in Revenue Change: \" +\"$\"+ str(average_change_revenue))\n",
    "print(\"Greatest Increase in Revenue:\" + str(max[0])+\" ($\" + str(max[1])+\")\")\n",
    "print(\"Greatest Decrease in Revenue:\" + str(min[0])+\" ($\" + str(min[1])+\")\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
