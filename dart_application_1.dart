// void main(List<String> arguments) {
//   print('Hello world: ${dart_application_1.calculate()}!');
// }

import 'dart:io';
import 'dart:math';

void main() {
  // int a = 6;
  // double b = 7.7;
  // // num= int and double

  // var name = "wdjkwjd"; /*оперделяет тип сам
  //                         (но не можем сами потом менять тип)*/
  // var name1 = 123;

  // String name12 = "ABFKhekhfehfkfewk";

  // bool govno = false;

  // int a1 = 606_905_488_694;
  // int a2 = 606905488694;

  // print(4.compareTo(5)); //Сравнивает 2 числа. Ответ: -1
  // print(5.compareTo(4)); // 1
  // print((-5).abs()); //модуль

  // print(-5.round()); //Округление
  // print(-5.7.round());
  // print(5.3.ceil()); //Округление в большую
  // print(5.3.floor()); //Округление в меньшую

  // print(6.isEven); //Четное
  // print(7.isOdd); //Нечетное

  // print(5.toRadixString(2)); //Система счисления. Есть 2.8.16

  // print((-5).isNegative);
  // print(4.bitLength); //Сколько битов занимает

  // print(30.gcd(12)); //НОД

  // int a11 = 1;
  // int b22 = 2;
  // print(a11 + b22);
  // print(a11 - b22);
  // print(a11 / b22);
  // print(a11 % b22);
  // print(a11 ~/ b22);
  // print(a11++);
  // print(++a11); //Добавляет потом возвращает
  // print(a11 >= b22);
  // print(a11 += b22);

  // bool c1 = (5 > 4) && (5 == 5);
  // bool c2 = (5 > 4) || (5 == 6);
  // print(c1);
  // print(c2);

  // print(c2 is int);
  // print(c2 is! int);

  // String nan = "GAndon";
  // int age = 9;
  // print(nan);
  // print(age);

  // stdout.write("wegewg");
  // stdout.write("efwwf");
  // stdin.readLineSync(); //Readline()
  // String? age1 = stdin.readLineSync();
  // String age2 = stdin.readLineSync()!; //Должно ввести значение всегда
  // int age3 = int.parse(age2);

  // final a232;
  // a232 = 5;
  // const pi = 3.14;

  // late String name4; //можно не хратить нул и потом ввести
  // name4 = "ligkg";

  // var val = "1234";
  // var valint = int.parse(val);
  // var valdouble = double.parse(val);
  // var valstring = valint.toString();

  // int? brqkhjbf = int.tryParse("12h41");

  //   print("Введите калл: ");
  //   var new12 = double.parse(stdin.readLineSync()!);
  //   print("Введите скидос: ");
  //   var bdsef = double.parse(stdin.readLineSync()!);
  //   var dwh = (new12*bdsef)/100;
  //   print("Привет $dwh");

  // String a = "Ivan";
  // String a1 = "JFOHFWfowfw";
  // String str = "П" + a.substring(1);
  // print(str);
  // print(str.toLowerCase());
  // print(a+str);
  // print(str*3);
  // print(str.compareTo(a1)); // Сравнение
  // print(str.contains('a')); //проверка на наличие
  // print(str.indexOf('v')); // Первый лемент вхождения, есть lastIndexof()
  // String aa = "Dart";
  // print(aa.trimRight()); //Удаляет пробелы
  //print(aa.split(' ')); //Разделяет строку
  // print(aa.length); //Дилна строки

  // String aaa = "Программирование на Dart";
  // print(aaa.length);

  // String aaaa = 'Dart';
  // String a11 = aaaa[0];
  // String a22 = aaaa[-1];

  // print("$a11, $a22");

  // String fgfg = " Dart ";
  // print(fgfg.trim());

  // String aq = "Быстрый коричневый лес";
  // print(aq.indexOf("коричневый"));

  // padLeft(); //Добавка слева справа символов

  // print("dart - sidjv idufv".split(" ").length);

  // var aaaaa = "анна".split('').reversed.join('');
  // var aaaaaa = "анна";
  // print(aaaaa.compareTo(aaaaaa));
  // aaaaaa.replaceAll(r'[0-6]', aaaaa);

  // if (условие)
  // {
  //   тело
  // }

  // int a = 7;
  // int b = 8;
  // if (a > b)
  // {
  //   print("Pizdec");
  // }
  // else if (a == b)
  // {
  //   print("ravni sychki");
  // }
  // else
  // {
  //   print("yra");
  // }

  // var a = 1;

  // switch (a) {
  //   case 1:
  //     print("chislo ravno 1");
  //     break;
  //   case 2:
  //     print("ujdyj");
  //     a++;
  //     continue n3; //Метка перехода на другой кейс
  //   n3:
  //   case 3:
  //     break;
  //   default:
  //     print("def");
  //     break;
  // }

  // double v = 9;
  // double d = 6;

  // double c = v > d ? v - d : v / d;
  // print(c);

  print("1 chislo: ");
  var a = double.parse(stdin.readLineSync()!);
  print("2 chislo: ");
  var b = double.parse(stdin.readLineSync()!);
  print("Метод");
  var met = stdin.readLineSync()!;

  if (met == "Ариф") {
    print("oper");
    var oper = stdin.readLineSync()!;

    switch (oper) {
      case "+":
        print(a + b);
        break;
      case "-":
        print(a - b);
        break;
      case "*":
        print(a * b);
        break;
      case "/":
        if (b != 0) {
          print(a / b);
        } else {
          print("Деление на 0");
        }
        break;
      case "%":
        if (b != 0) {
          print(a % b);
        } else {
          print("Деление на 0");
        }
        break;
      case "~/":
        if (b != 0) {
          print(a ~/ b);
        } else {
          print("Деление на 0");
        }
        break;
      case "pow":
        print(pow(a, b));
        break;
    }
  } else if (met == "Срав") {
    print("oper");
    var oper = stdin.readLineSync()!;
    switch (oper) {
      case "==":
        print(a == b);
        break;
      case '!=':
        print(a != b);
        break;
      case '>':
        print(a > b);
        break;
      case '<':
        print(a < b);
        break;
      case '>=':
        print(a >= b);
        break;
      case '<=':
        print(a <= b);
        break;
    }
  } else if (met == "Логика") {
    print("oper");
    var oper = stdin.readLineSync()!;
    print('Проверка на уровнение');
    switch (oper) {
      case "&&":
        print(a % b == 0 && a / 2 == 0);
        break;
      case "||":
        print(a % b == 0 || a / 2 == 0);
        break;
      case "!":
        print(a % b != 0 && a / 2 != 0 && b / 2 != 0);
        break;
    }
  }
}
