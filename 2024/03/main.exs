defmodule Aoc2024D3 do
  def input(filename) do 
    File.read(filename) 
    |> elem(1) 
  end
end

input = Aoc2024D3.input("input.d3")
Regex.scan(~r/mul\(\d+,\d+\)/, input)
|> Enum.reduce(0, fn str, sum -> 
  Regex.scan(~r/\d+/, to_string(str))
  |> List.flatten() 
  |> Enum.reduce(1, fn e, product -> 
    e
    |> String.to_integer()
    |> Kernel.*(product)
  end)
  |> Kernel.+(sum)
end)
|> IO.inspect()


input = Aoc2024D3.input("input.d3")
l = Regex.scan(~r/mul\(\d+,\d+\)|do\(\)|don\'t\(\)/, input)
|> Enum.reduce({[], []}, fn str, {l, vals} -> 
    str = to_string(str)
    {[cond do  
      String.starts_with?(str, "don't") -> false
      String.starts_with?(str, "do") -> true
      Enum.empty?(l) -> true
      true -> List.first(l)
    end | l], [str | vals]}
  end)
Enum.zip(elem(l, 0), elem(l, 1))
|> Enum.filter(fn {a, b} -> 
  cond do
    String.starts_with?(b, "do") -> false
    a -> true
    1 -> false
  end
end)
|> Enum.reduce(0, fn {_, str}, sum -> 
  Regex.scan(~r/\d+/, to_string(str))
  |> List.flatten() 
  |> Enum.reduce(1, fn e, product -> 
    e
    |> String.to_integer()
    |> Kernel.*(product)
  end)
  |> Kernel.+(sum)
end)
|> IO.inspect()
