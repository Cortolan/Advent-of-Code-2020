/*
Day 5 - Advent of code prompts - https://adventofcode.com/2020/day/5

Written by Corbin Ortolan

*/

#include <iostream>
#include <math.h>
#include <fstream>
#include <vector>
#include <algorithm>

int return_middle (double start, double end, char round)
{
    if (round == 'B' || round == 'R')
        return (ceil((end - start)/2) + start);
    else
        return (floor((end - start)/2) + start);
}


int find_row(std::string seat_code_row)
{
    int start = 0;
    int end = 127;
    
    for (int i = 0; i < seat_code_row.length()-1; i++)
    { 
        if (seat_code_row[i] == 'F')
            end = return_middle(start, end, seat_code_row[i]);
        else
            start = return_middle(start,end, seat_code_row[i]);
    }

    if(seat_code_row[seat_code_row.length()-1] == 'F')
        return int(start);
    else
        return int(end);   
}

int find_column(std::string seat_code_column)
{
    double start = 0;
    double end = 7;

    for (int i = 0; i < seat_code_column.length() -1; i++)
    {
        if (seat_code_column[i] == 'R')
            start = return_middle(start, end, seat_code_column[i]);
        else
            end = return_middle(start, end, seat_code_column[i]);
    }

    if (seat_code_column[seat_code_column.length() -1] == 'R')
           return int(end);
        else
            return int(start);
}

int find_seat_id(std::string seat_code)
{
    int column_code_index = seat_code.length() - 3; 

    std::string seat_code_row = seat_code.substr(0, column_code_index);
    std::string seat_code_column = seat_code.substr(column_code_index, seat_code.length() - 1);

    int row = find_row(seat_code_row);
    int column =  find_column(seat_code_column);

    return (row * 8 + column);
}

int find_missing_seat(std::vector<int> all_seats)
{
    int desired_sum = 0, sum = 0;

    for (int i = 0; i < all_seats.size(); i++)
    {
        sum += all_seats[i];
    }

    for (int i = all_seats[0]; i <= all_seats.back(); i++)
    {
        desired_sum += i;
    }

    return desired_sum - sum;
}

int main()
{
    std::ifstream input_data;
    input_data.open ("Data/day5_data.txt", std::ifstream::in);

    std::vector<int> all_seats;
    int missing_seat = -1;

    if (input_data)
    {
        std::string input_line;
        while (std::getline(input_data, input_line))
        {
            all_seats.push_back(find_seat_id(input_line));          
        }

        std::sort(all_seats.begin(),all_seats.end());
        missing_seat = find_missing_seat(all_seats);

        std::cout << "Part 1: Largest Seat ID: " << all_seats.back();
        std::cout << "Part 2: Find missing seat in center of plane: " << missing_seat;
    }
    else
        std::cout << "Falied to open file";
}