/*
Advent of code Day 6 - https://adventofcode.com/2020/day/6

Written by Corbin Ortolan
*/

#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <map>

int count_group_total_answers(std::vector<std::string> group)
{
    std::vector<char> answered_questions;
    
    for (int person = 0; person < group.size(); person++)
    {
        for(int question = 0; question < group[person].length(); question++)
        {
            if (std::find(answered_questions.begin(), answered_questions.end(), group[person][question]) != answered_questions.end())
            {
                //do nothing
            }
            else
            {
                answered_questions.push_back(group[person][question]);
            }
        }    
    }

    return answered_questions.size();
}

int count_group_answered_the_same_question(std::vector<std::string> group)
{
    std::map<char,int> answered_questions;
    int count = 0;

    for (int i = 0; i < group[0].length(); i++)
    {
        answered_questions[group[0][i]] = 1;
    }

    for (int person = 1; person < group.size(); person++)
    {
        for(int question = 0; question < group[person].length(); question++)
        {
            if (answered_questions[group[person][question]])
            {
                answered_questions[group[person][question]] += 1;
            }
        }    
    }
    
    for (int i = 0; i < group[0].length(); i++)
    {
        if (answered_questions[group[0][i]] == group.size())
            count +=1;        
    }
    return count;
}

int main()
{
    std::ifstream input_data;
    input_data.open ("Data/day6_data", std::ifstream::in);

    if (input_data)
    {
        std::vector<std::string> group;
        std::string input_line;

        int total_answered_questions = 0, total_group_questions_answered_the_same = 0;
        
        while (std::getline(input_data, input_line))
        {   
            if (input_line == "")
            {
                total_answered_questions += count_group_total_answers(group);
                total_group_questions_answered_the_same += count_group_answered_the_same_question(group);
                group.clear();
            }
            else
            {
              group.push_back(input_line);
            }
        }
 
        total_answered_questions += count_group_total_answers(group);
        total_group_questions_answered_the_same += count_group_answered_the_same_question(group);
        std::cout << "Part 1 - Total answered questions all groups: " << total_answered_questions;
        std::cout << "Part 2 - Total answered questions all groups answered all the same questions: " << total_group_questions_answered_the_same;
    }
    else
    {
        std::cout << "Failed to open file";
    }
    
}